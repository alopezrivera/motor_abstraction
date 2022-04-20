import logging
import traceback
from functools import wraps

from motor_abstraction.utils.shout import shout_error, shout_disabled


def fallback_disable(goal):

        def decorator(fn):
            
            @wraps(fn)
            def _impl(self, *method_args, **method_kwargs):

                try:
                    return fn(self, *method_args, **method_kwargs)
                except Exception as e:
                    shout_error(goal)
                    logging.error(traceback.format_exc())
                    self.disable()

            return _impl

        return decorator