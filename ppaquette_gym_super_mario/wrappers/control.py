import gym

__all__ = ['set_playing_mode']


def set_playing_mode(target_mode):
    """ target mode can be 'algo' or 'human' """

    class SetPlayingModeWrapper(gym.Wrapper):
        """
            Doom wrapper to change playing mode 'human' or 'algo'
        """

        def __init__(self, env):
            super(SetPlayingModeWrapper, self).__init__(env)
            if target_mode not in ['algo', 'human']:
                raise gym.error.Error(
                    'Error - The mode "{}" is not supported. Supported options are "algo" or "human"'.format(
                        target_mode))
            self.unwrapped.mode = target_mode

    return SetPlayingModeWrapper
