import application
import tempfile
from unittest import mock

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = application.Application()
    context.temp_journal_file = tempfile.NamedTemporaryFile()
    context.application.journal_file = context.temp_journal_file.name

@given("composed text is")
def step_impl(context):
    context.application.edit = mock.Mock(return_value=context.text)

@given("time is \"{time}\"")
def step_impl(context, time):
    context.application.time = mock.Mock(return_value=time)

@when("run application")
def step_impl(context):
    context.application.run()

@then("should edit text")
def step_impl(context):
    assert context.application.edit.call_count == 1

@then("content of journal is")
def step_impl(context):
    assert context.application.journal == context.text, \
        "{0} != {1}".format(context.application.journal, context.text)

@then("content of journal file is")
def step_impl(context):
    with open(context.application.journal_file, "r") as f:
        text = f.read()
        assert text == context.text, \
            "{0} != {1}".format(text, context.text)
