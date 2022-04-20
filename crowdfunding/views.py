from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Products


# Create your views here.
products = Products()

def index(request):
    return HttpResponse("Hello, Welcome to CrowdFunding.")

@csrf_exempt
def addProducts(request):
    if request.method == 'GET':
        article = '''
            <form action="/add/" method="post">
                <p><input type="text" name="postTitle" placeholder="게시글 제목" /></p>
                <p><input type="text" name="publisherName" placeholder="게시자 명" /></p>
                <p><input type=text"" name="productDesc" placeholder="상품 설명" /></p>
                <p><input type="int" name="targetAmount" placeholder="목표 금액" /></p>
                <p><input type="date" name="endDate" placeholder="펀딩 종료일" /></p>
                <p><input type="int" name="amountPerTimes" placeholder="1회 펀딩 금액" /></p>
                <p><input type="submit"/></p>
            </form>
        '''
        # return request.method.GET

    elif request.method == 'POST':
        products.postTitle = request.POST['postTitle']
        products.publisherName = request.POST['publisherName']
        products.productDesc = request.POST['productDesc']
        products.targetAmount = request.POST['targetAmount']
        products.endDate = request.POST['endDate']
        products.amountPerTimes = request.POST['amountPerTimes']

        # products 테이블 내 id가 있을 경우 하나씩 증가, 아니면 0으로 초기값을 가짐
        id_list = list(map(lambda x: x.postId, products.objects.all()))
        products.postId = max(id_list) + 1 if id_list else 0
        products.save()
        return redirect('/')

@csrf_exempt
def editProducts(request, id):
    if request.method == 'GET':
        product = Products.objects.get(postId=id)
        article = f'''
            <form action="/edit/{id}" method="post">
                <p><input type="text" name="postTitle" placeholder="게시글 제목" /></p>
                <p><input type="text" name="publisherName" placeholder="게시자 명" /></p>
                <p><input type=text"" name="productDesc" placeholder="상품 설명" /></p>
                <p><input type="date" name="endDate" placeholder="펀딩 종료일" /></p>
                <p><input type="int" name="amountPerTimes" placeholder="1회 펀딩 금액" /></p>
                <p><input type="submit"/></p>
            </form>
        '''
        # return request.method.GET

    elif request.method == 'POST':
        product = Products.objects.get(postId=id)
        product.postTitle = request.POST['postTitle']
        product.publisherName = request.POST['publisherName']
        product.productDesc = request.POST['productDesc']
        if product.targetAmount != request.POST['targetAmount']:
            print("목표 금액은 변경이 불가합니다.")
            product.targetAmount = product.targetAmount
        product.endDate = request.POST['endDate']
        product.amountPerTimes = request.POST['amountPerTimes']
        product.save()
        return redirect(f'/show/{id}')

@csrf_exempt
def deleteProducts(request):
    if request.method == 'POST':
        id = int(request.POST['postId'])
        product = Products.objects.get(postId=id)
        product.delete()
        return redirect('/')