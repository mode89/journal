import application
import tempfile
from unittest import mock

@given("not implemented")
def step_impl(context):
    raise NotImplemented

@given("application")
def step_impl(context):
    context.application = application.Application()
    context.temp_journal = tempfile.NamedTemporaryFile()
    context.application.config["journal"] = context.temp_journal.name

@given("composed text is")
def step_impl(context):
    context.application.edit = mock.Mock(return_value=context.text)

@given("time is \"{time}\"")
def step_impl(context, time):
    context.application.time = mock.Mock(return_value=time)

@given("load config from file \"{name}\"")
def step_impl(context, name):
    context.application.load_config(name)

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
    with open(context.application.config["journal"], "r") as f:
        text = f.read()
        assert text == context.text, \
            "{0} != {1}".format(text, context.text)

@then("journal file name is \"{name}\"")
def step_impl(context, name):
    assert context.application.config["journal"] == name
