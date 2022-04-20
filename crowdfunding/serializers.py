from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Products


# 기본적으로 제공되는 유저를 RESTAPI 하기 위한 설정
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


# 상품 등록, 수정, 펀딩
class AddProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "postTitle",
            "publisherName",
            "productDesc",
            "targetAmount",
            "endDate",
            "amountPerTimes",
        ]


class EditProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "postTitle",
            "publisherName",
            "productDesc",
            "endDate",
            "amountPerTimes",
        ]


class FundProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ["amountPerTimes"]


class ProductsSerializer(serializers.ModelSerializer):
    # now()와 endDate를 timedelta 사용해서 d-day 구하기
    DDay = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            "postId",
            "postTitle",
            "publisherName",
            "productDesc",
            "targetAmount",
            "startDate",
            "endDate",
            "amountPerTimes",
            "totalAmount",
            "achievementRate",
            "participantCount",
        ]

        extra_kwargs = {
            "targetAmount": {"read_only": True},
        }

    def DDay(self, instance):
        return instance.DDay()