import string
import subprocess
import tempfile

from approvaltests import verify, set_default_reporter, DiffReporter
from approvaltests.reporters import PythonNativeReporter, ReportWithDiffCommandLine, GenericDiffReporter


def test_1() -> None:
    outputs = run_golden_master("test1")
    verify(outputs)


def test_2() -> None:
    outputs = run_golden_master("test2")
    verify(outputs)


def test_3() -> None:
    outputs = run_golden_master("test3")
    verify(outputs)


def run_golden_master(test: string) -> string:
    cmd = "python ./test/golden_master/%s.py" % test
    with tempfile.TemporaryFile(mode='w+') as output:
        proc = subprocess.Popen(cmd, stdout=output, shell=True)
        proc.wait()
        output.seek(0)
        result = output.read()
        output.close()
    return result
