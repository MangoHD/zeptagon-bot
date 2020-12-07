# ------------------------ Modules ------------------------ #

import discord
import asyncio
import random
import datetime
import os
import json
import PIL
import math
import pyfiglet
import requests
import re
import base64
import dyv_math as mfmath
from boto.s3.connection import S3Connection
from PIL import Image
from io import BytesIO
from discord.ext import commands


prefix = ["Z/","z/"]
client = commands.Bot(command_prefix=prefix, intents=intents, case_insensitive= True)
