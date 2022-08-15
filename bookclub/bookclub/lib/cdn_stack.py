from aws_cdk import (
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3 as s3,
    RemovalPolicy,
    Stack
)

class Hosting(Stack):
    def __init__(
        self,
        scope,
        construct_id,
        **kwargs,
    ):
        super().__init__(scope, construct_id, **kwargs)
        self._create_site_bucket()
        self._create_cloudfront_distribution()

    def _create_site_bucket(self):
        self.site_bucket = s3.Bucket(
            self,
            "site_bucket",
            bucket_name="thebookclubassets",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

    def _create_cloudfront_distribution(self):
        self.distribution = cloudfront.Distribution(
            self,
            "cloudfront_distribution",
            default_behavior=cloudfront.BehaviorOptions(
                allowed_methods=cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
                origin=origins.S3Origin(self.site_bucket),
                viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            ),
            default_root_object="index.html",
        )