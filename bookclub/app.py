#!/usr/bin/env python3
import sys

import aws_cdk as cdk

from bookclub.bookclub_stack import TheBookClubStack

app = cdk.App()
TheBookClubStack(app, "TheBookClubStack")
app.synth()
