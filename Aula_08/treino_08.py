from loguru import logger

logger.add("meu_app.log", rotation="5 MB")

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f'Chamando {func.__name__} com {args} e {kwargs}')
        try:
            result = func(*args,**kwargs)
            logger.info(f'{func.__name__} retornou {result}')
            return result
        except Exception as e:
                logger.exception(f'{func.__name__} lançou uma exceção {e}')
                raise
    return wrapper



@log_decorator
def soma(a, b):
     return a + b


@log_decorator
def falha():
     raise ValueError('Um erro intencional')


soma(3, 3)

try:
     falha()
except ValueError:
     pass
