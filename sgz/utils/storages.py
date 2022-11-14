from storages.backends.s3boto3 import S3Boto3Storage


class StaticRootS3Boto3Storage(S3Boto3Storage):  # skipcq: PYL-W0223
    location = "static"
    default_acl = "public-read"


class MediaRootS3Boto3Storage(S3Boto3Storage):  # skipcq: PYL-W0223
    location = "media"
    file_overwrite = False
