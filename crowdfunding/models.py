from django.db import models
import datetime

# Create your models here.
class Products(models.Model):
    postId = models.PositiveIntegerField(primary_key=True, verbose_name='게시글 ID'),
    postTitle = models.CharField(blank=True, max_length=255, verbose_name='게시글 제목'),
    publisherName = models.CharField(blank=True, max_length=30, verbose_name='게시자 명'),
    productDesc = models.CharField(blank=True, max_length=500, verbose_name='상품 설명'),
    targetAmount = models.PositiveIntegerField(null=True, verbose_name='목표 금액'),
    startDate = models.DateTimeField(auto_now_add=True, verbose_name='펀딩 시작일'),
    endDate = models.DateField(default=datetime.date.today() + datetime.timedelta(days=14), verbose_name='펀딩 종료일'),
    amountPerTimes = models.PositiveIntegerField(null=True, verbose_name='1회 펀딩 금액'),
    totalAmount = models.PositiveIntegerField(default=0, verbose_name='총 펀딩 금액'),
    achievementRate = models.PositiveIntegerField(default=0, verbose_name='달성률'),
    participantCount = models.PositiveIntegerField(default=0, verbose_name='참여자 수')

    class Meta:
        managed = False
        db_table = 'products'
