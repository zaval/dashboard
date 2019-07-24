import sys
import pkgutil

__all__ = []
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
    __all__.append(module_name)
    _module = loader.find_module(module_name).load_module(module_name)
    globals()[module_name] = _module

serviceEnums = (
    ("AS", "Google AdSense"),
    ("KC", "KeyCDN"),
    ("RN", "RamNode"),
    ("HS", "Hostens"),
    # ("DN", "DNSMadeEasy"),
)


class ParseService:
    def __init__(self, name):
        self.m = None

        for e in serviceEnums:
            if e[0] == name:
                class_name = e[1].replace(" ", "_")

                for i in __all__:
                    try:
                        modi = sys.modules[i]
                        self.m = getattr(modi, class_name)()
                        print(self.m)
                        break
                    except:
                        # print(e)
                        continue

    def start(self, login, password, data):
        if self.m:
            return self.m.start(login, password, data)
        else:
            return {}
