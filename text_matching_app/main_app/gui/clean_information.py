from confirmations import error_message
from button_commands import ButtonCommands
from pathlib import Path


class CleanInformation(ButtonCommands):

    def __location(self) -> Path:

        location: Path = Path(self.collect_information()[0])
        if location.exists():
            return location
        else:
            print(

                error_message(

                    title='location error',
                    error='the location you entered is invalid!!!'

                )
            )

            self.clear_all()

    def __regex_date(self) -> str:
        return self.collect_information()[1]

    def __regex_name(self) -> str:
        return self.collect_information()[2]

    def __regex(self) -> str:
        return self.collect_information()[3]

    def submit_information(self) -> tuple[Path, str, str, str]:
        return self.__location(), self.__regex_date(), self.__regex_name(), self.__regex()
