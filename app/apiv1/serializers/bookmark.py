from app.bookmark.models import Bookmark, AccountBookmark
from app.accounts.models import Account
from rest_framework import serializers, fields

class BookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = (
            'id',
            'title',
            'image',
            'description',
            'theme',
        )

class AccountBookmarkSerializer(serializers.ModelSerializer):
    account_name = serializers.SerializerMethodField()
	
    class Meta:
        model = Bookmark
        fields = (
            'id',
            'title',
            'image',
            'description',
            'theme',
            'account_name',
        )

    def get_account_name(self, obj):
        user = self.context.get('user')
        qs = Account.objects.filter(id=user).first()

        return qs.preferred_name
