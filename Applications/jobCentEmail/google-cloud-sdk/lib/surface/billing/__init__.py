# -*- coding: utf-8 -*- #
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Commands for managing billing accounts and associate them with projects."""
from __future__ import absolute_import
from __future__ import unicode_literals
from googlecloudsdk.calliope import base


@base.ReleaseTracks(base.ReleaseTrack.ALPHA, base.ReleaseTrack.BETA)
class Billing(base.Group):
  """Manage billing accounts and associate them with projects.

  Manage billing accounts and associate them with projects.

  ## EXAMPLES

  To list billing accounts associated with the current user, run:

    $ {command} accounts list

  To link one of the billing accounts `0X0X0X-0X0X0X-0X0X0X` with a project
  `my-project`, run:

    $ {command} projects link my-project --billing-account 0X0X0X-0X0X0X-0X0X0X
  """

  def Filter(self, context, args):
    del context, args
    base.DisableUserProjectQuota()
