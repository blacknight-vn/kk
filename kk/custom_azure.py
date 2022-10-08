from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'djangoaccountstorage1221'
    account_key = 'zJIrI7c870aeqlYfXP60IkKC7VajSd6sl1sbYUOxmNFGCLgw4/W2FEaoKb0+rPperWTJM3WQ4Xhj+AStkIlKRA=='
    azure_container = 'media2'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'djangoaccountstorage1221'
    account_key = 'zJIrI7c870aeqlYfXP60IkKC7VajSd6sl1sbYUOxmNFGCLgw4/W2FEaoKb0+rPperWTJM3WQ4Xhj+AStkIlKRA=='
    azure_container = 'static'
    expiration_secs = None