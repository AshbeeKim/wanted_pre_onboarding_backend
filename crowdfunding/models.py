from django.db import models
import datetime

# Create your models here.
class Products(models.Model):
    postId = models.PositiveIntegerField('게시글 ID', primary_key=True, auto_created=True)
    postTitle = models.CharField('게시글 제목', blank=True, max_length=255)
    publisherName = models.CharField('게시자 명', blank=True, max_length=30)
    productDesc = models.CharField('상품 설명', blank=True, max_length=500)
    targetAmount = models.PositiveIntegerField('목표 금액', editable=False)
    startDate = models.DateTimeField('펀딩 시작일', auto_now_add=True)
    endDate = models.DateField('펀딩 종료일', default=datetime.date.today)
    amountPerTimes = models.PositiveIntegerField('1회 펀딩 금액', null=True)
    totalAmount = models.PositiveIntegerField('총 펀딩 금액', default=0, null=True)
    achievementRate = models.PositiveIntegerField('달성률', default=0, null=True)
    participantCount = models.PositiveIntegerField('참여자 수', default=0, null=True)

    class Meta:
        db_table = 'products'

