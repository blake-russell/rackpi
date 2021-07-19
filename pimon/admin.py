# Register your models here.

from django.contrib import admin
from .models import Miner
from .models import Coin
from .models import Myrig
from .models import Mypool
from .models import Mypdu
from .models import ConfigGlobal
from .models import ConfigPool
from .models import ConfigTicker
from .models import ConfigTemp
from .models import ConfigForecast
from .models import ConfigWtm
from .models import ConfigWallet


admin.site.register(Miner)
admin.site.register(Coin)
admin.site.register(Myrig)
admin.site.register(Mypool)
admin.site.register(Mypdu)
admin.site.register(ConfigGlobal)
admin.site.register(ConfigPool)
admin.site.register(ConfigTicker)
admin.site.register(ConfigTemp)
admin.site.register(ConfigForecast)
admin.site.register(ConfigWtm)
admin.site.register(ConfigWallet)