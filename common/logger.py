import logging

def get_logger(name="api_test"):
    logger=logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if logger.handlers:
        return logger

    fmt=logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s',
                          datefmt='%Y-%m-%d %H:%M:%S')

    ch=logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fh=logging.FileHandler('api_test.log',encoding='utf-8',mode='w')
    fh.setLevel(logging.DEBUG)

    ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger