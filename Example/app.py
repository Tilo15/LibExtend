from LibExtend import ExtensionCatalogue

extensions_catalogue = ExtensionCatalogue("net.unitatem.libextend.example", ["Example/Extensions"], False)

extensions = extensions_catalogue.get_all("Greeting")

for extension in extensions:
    greeting_extension = extension.get()
    greeting_instance = greeting_extension()
    print("Hello %s!" % greeting_instance.get_greeting_subject())

best_extension = extensions_catalogue.best("Greeting").get()

best_instance = best_extension()
print("Best ranking: %s" % best_instance.get_greeting_subject())