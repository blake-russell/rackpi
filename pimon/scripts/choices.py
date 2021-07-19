from django.utils.translation import gettext as _

# Create choice lists to be called into models, views, etc...

ASIC = 'ASIC'
sFPGA = 'sFPGA'
cFPGA = 'cFPGA'
GPU = 'GPU'
MINER_TYPE = (
	(ASIC, _("ASIC")),
	(sFPGA, _("FPGA")),
	(cFPGA, _("cFPGA")),
	(GPU, _("GPU")),
	)

MINER_ALG = (
	("SHA-256", _("SHA-256")),
	("Ethash", _("Ethash")),
	("Scrypt", _("Scrypt")),
	("X11", _("X11")),
	("Equihash", _("Equihash")),
	("Zhash", _("Zhash")),
	("CryptoNightLiteV1", _("CryptoNightLiteV1")),
	("CryptoNightV7", _("CryptoNightV7")),
	("Blake (14r)", _("Blake (14r)")),
	("Blake (2b)", _("Blake (2b)")),
	("LBRY", _("LBRY")),
	("Pascal", _("Pascal")),
	("Lyra2REv2", _("Lyra2REv2")),
	("Myr-Groestl", _("Myr-Groestl")),
	("Qubit", _("Qubit")),
	("Quark", _("Quark")),
	("Skein", _("Skein")),
	("Nist5", _("Nist5")),
	("TimeTravel10", _("TimeTravel10")),
	("PHI1612", _("PHI1612")),
	("PHI2", _("PHI2")),
	("X16R", _("X16R")),
	("NeoScrypt", _("NeoScrypt")),
	("X11Gost", _("X11Gost")),
	("Any", _("Any")),
	("None", _("None")),
	)

CCMINER = "ccminer"
CGMINER = "cgminer"
SGMINER = "sgminer"
BGMINER = "bgminer"
BMMINER = "bmminer"
BFGMINER = "bfgminer"
ETHMINER = "ethminer"
NONE = "NONE"
MINER_SOFTWARE = (
	(CCMINER, _("ccminer")),
	(CGMINER, _("cgminer")),
	(SGMINER, _("sgminer")),
	(BGMINER, _("bgminer")),
	(BMMINER, _("bmminer")),
	(BFGMINER, _("bfgminer")),
	(ETHMINER, _("ethminer")),
	(NONE, _("NONE")),
	)

YES = "yes"
NO = "no"
YES_OR_NO = (
	(YES, _("yes")),
	(NO, _("no")),
	)

GMAIL = "Gmail"
OTHER = "Other"
EMAIL_TYPE = (
	(GMAIL, _("Gmail")),
	(OTHER, _("Other")),
	)

ONLINE = "Online"
OFFLINE = "Offline"
ONLINE_OR_OFFLINE = (
	(ONLINE, _("Online")),
	(OFFLINE, _("Offline")),
	)

GPIO_PIN = (
	(-1, _("NONE")),
	(0, _("0")),
	(1, _("1")),
	(2, _("2")),
	(3, _("3")),
	(4, _("4")),
	(5, _("5")),
	(6, _("6")),
	(7, _("7")),
	(8, _("8")),
	(9, _("9")),
	(10, _("10")),
	(11, _("11")),
	(12, _("12")),
	(13, _("13")),
	(14, _("14")),
	(15, _("15")),
	(16, _("16")),
	(17, _("17")),
	(18, _("18")),
	(19, _("19")),
	(20, _("20")),
	(21, _("21")),
	(22, _("22")),
	(23, _("23")),
	(24, _("24")),
	(25, _("25")),
	(26, _("26")),
	(27, _("27")),
	)

PDUMODULE = "PDU/Power"
FORECASTMODULE = "Forecast"
TEMPMODULE = "Ambient Temps"
WTMMODULE = "Whattomine Module"
PROFITMODULE = "Profit Monitor"
WALLETMODULE = "Wallet Module"
POOLMODULE = "Pool Monitor"
ASICMODULE = "ASIC Monitor"
GPUMODULE = "GPU Monitor"
TICKERMODULE = "Price Ticker"
IFRAMEMODULE = "iFrame Module"
LOAD_MODULE = (
	(PDUMODULE, _("PDU/Power")),
	(FORECASTMODULE, _("Forecast")),
	(TEMPMODULE, _("Ambient Temps")),
	(WTMMODULE, _("Whattomine Module")),
	(PROFITMODULE, _("Profit Monitor")),
	(WALLETMODULE, _("Wallet Module")),
	(POOLMODULE, _("Pool Monitor")),
	(ASICMODULE, _("ASIC Monitor")),
	(GPUMODULE, _("GPU Monitor")),
	(TICKERMODULE, _("Price Ticker")),
	(IFRAMEMODULE, _("iFrame Module")),
	)

PDU_TYPE = (
	("HP_S124", _("HP S124")),
	)

CALL_TYPE = (
	("SNMPv2c", _("SNMPv2c")),
	("SNMPv3", _("SNMPv3")),
	("JSON", _("JSON")),
	)

TEMP_READING = (
	("Fahrenheit", _("Fahrenheit")),
	("Celsius", _("Celsius")),
	)

TEMP_MODEL = (
	("DHT11", _("DHT11")),
	("DHT22", _("DHT22")),
	("AM2302", _("AM2302")),
	("AM2302", _("AM2302")),
	("DS18B20", _("DS18B20"))
	)

FORECAST_SITE = (
	("OpenWeatherMap", _("OpenWeatherMap")),
	("None", _("None")),
	)