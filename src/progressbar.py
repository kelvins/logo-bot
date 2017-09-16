
import sys


class ProgressBar(object):

    def __init__(self, total, prefix="Progress:", suffix="Complete", decimals=2, bar_length=50, char="#"):
        """
        This class is used to show a progress bar.
        :param total: the total value of the progress bar (e.g. 100%)
        :param prefix: the prefix shown before the progress bar (default is 'Progress:')
        :param suffix: the suffix shown after the progress bar (default is 'Complete')
        :param decimals: the number of decimal places (default is 2)
        :param bar_length: the length/width of the progress bar (default is 50)
        :param char: the char that will be used to fill the progress bar (default is #)
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.bar_length = bar_length
        self.char = char

    def update(self, progress):
        """
        Function used to update the progress bar.
        :param progress: the current progress (should be lower than the total)
        """

        # Check if the progress is valid
        if progress < 0:
            progress = 0
        elif progress > self.total:
            progress = self.total

        str_format = "{0:." + str(self.decimals) + "f}"
        percents = str_format.format(100 * (progress / float(self.total)))
        filled_length = int(round(self.bar_length * progress / float(self.total)))
        bar = self.char * filled_length + '-' * (self.bar_length - filled_length)

        sys.stdout.write('\r%s |%s| %s%s %s' % (self.prefix, bar, percents, '%', self.suffix))

        # If the progress is equal or higher than the total, break the line
        if progress >= self.total:
            sys.stdout.write('\n')
        sys.stdout.flush()
