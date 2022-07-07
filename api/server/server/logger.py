import logging
import time


def LoggerDec(return_res=True, show_args=True):

    def decorator(func, *args, **kwargs):
        logger = logging.getLogger('django')

        def wrapper(*args, **kwargs):
            start = time.time()
            if show_args:
                logger.info(f'Resolver "{func.__qualname__}" started with {kwargs}')
            else:
                logger.info(f'Resolver "{func.__qualname__}" started')

            try:
                res = func(*args, **kwargs)
                finish = time.time()
                if return_res:
                    logger.info(f'Resolver "{func.__qualname__}" finished in {finish - start} sec with result {res}')
                else:
                    logger.info(f'Resolver "{func.__qualname__}" finished in {finish - start} sec')

            except Exception as exc:
                finish = time.time()
                logger.error(f'Resolver "{func.__qualname__}" crashed with Exception {exc} in {finish - start} sec')
                return ''

            return res

        return wrapper

    return decorator
