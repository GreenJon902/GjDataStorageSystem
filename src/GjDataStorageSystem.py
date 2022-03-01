import os

if __name__ == "__main__":
    import betterLogger
    base_logger = betterLogger.get_logger("BaseLogger")

    base_logger.log_info("Setting up kivy")
    os.environ["KIVY_NO_FILELOG"] = "True"
    os.environ["KIVY_NO_CONSOLELOG"] = "True"
    # noinspection PyUnresolvedReferences
    import kivy

    base_logger.log_info("Setup Kivy!")
    base_logger.log_info("Starting...")

    from gjDataStorageSystemApp import GjDataStorageSystemApp

    gjDataStorageSystemApp = GjDataStorageSystemApp()
    gjDataStorageSystemApp.run()
