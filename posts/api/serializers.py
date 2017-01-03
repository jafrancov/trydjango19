from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from posts.models import Post


post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
    )


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'user',
            'url',
        ]


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    # delete_url = HyperlinkedIdentityField(
    #     view_name='posts-api:delete',
    #     lookup_field='slug'
    # )
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'publish',
            'url',
            # 'delete_url',
        ]
