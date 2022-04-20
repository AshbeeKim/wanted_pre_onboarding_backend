from django.http import Http404
from .models import Products
from .serializers import (
    ProductsSerializer,
    AddProductsSerializer,
    EditProductsSerializer,
)
from rest_framework import (
    status,
    permissions,    # user, group 에 대한 이해가 높아지면 사용할 예정
)
from rest_framework.views import APIView
from rest_framework.response import Response


def get_object(id):
    try:
        return Products.objects.get(postId=id)
    except Products.DoesNotExist:
        raise Http404("주어진 게시글 ID로 등록된 게시글이 없습니다.")

class ProductsList(APIView):
    def get(self, request, format=None):
        products = Products.objects.all()
        if request.query_params.get("search"):
            keyword = request.query_params.get("search")
            products = Products.objects.filter(postTitle__contains=keyword)
        elif request.query_params.get("order_by"):
            keyword = request.query_params.get("order_by")
            assert keyword in ["생성일", "총펀딩금액"]  # 주어진 조건 외의 정렬 요청은 에러 발생
            if keyword == "생성일":
                products = Products.objects.all().order_by("startDate")
            elif keyword == "총펀딩금액":
                products = Products.objects.all().order_by("-totalAmount")

            serializer = ProductsSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        data = request.data
        data["publisherName"] = request.user.id
        serializer = AddProductsSerializer(data=data)
        if serializer.is_valid():
            serializer.save(publisherName=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetail(APIView):
    def get(self, request, id, format=None):
        product = get_object(id=id)
        serializer = ProductsSerializer(product)
        return Response(serializer.data)

    def delete(self, request, id, format=None):
        product = get_object(id=id)
        # 작성자인 경우에 지우는 코드는 알고 있지만, 운영자가 허위 펀딩이라 판단하고 지우는 내용을 반영하기는 아직 어려워서 우선은 주석 처리
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, id, format=None):
        product = get_object(id=id)
        # 위와 동일한 이유로 주석 처리 + 작성자와 동일한 그룹 중에서도 수정 권한이 있는 사람이 수정하도록 하는 코드를 반영하기 아직 어려움
        serializer = EditProductsSerializer(product, data=request.data, partial=True)
        # targetAmount 고정 값 반영이 안 된 것으로 보임.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsFunding(APIView):
    def patch(self, request, id, format=None):
        product = get_object(id=id)
        product.participantCount += 1   # 주어진 요구사항에선 단순 인원 수를 구하는 것이기에 용량을 적게 차지하는 방법 사용
        product.totalAmount += product.amountPerTimes
        product.save()
        return Response(status=status.HTTP_200_OK)

