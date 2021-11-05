#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "f885bc12-747f-49d2-8a7a-b9b712904ce8")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "sX&=rEA3VU2KMExY*fG$k2yHVgXm=jKrVFNTEFsc")
