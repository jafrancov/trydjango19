from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField, SerializerMethodField

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'object_id',
            'content_type',
            'parent',
            'content',
            'reply_count',
            'timestamp',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'content',
            'timestamp',
        ]


class CommentDetailSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    replies = SerializerMethodField()

    class Meta:
        model = Comment
        fields = [
            'id',
            'object_id',
            'content_type',
            'content',
            'reply_count',
            'replies',
            'timestamp',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        else:
            return None
