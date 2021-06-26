foo.Bar() assumes foo and bar are in the same process
if later you want to put all foo-related operations into a separate process, proxy allows you to do that without changing the interface

Proxy: class that functions as an interface to a resource. This can be remote, expensive to construct or requiring logging etc.

many types:
protection proxy - restricts access
virtual proxy - appears as the object it represents but behaves differently

Proxy vs decorator:
proxy keeps the same interface, decorator enhances it usually
decorator has reference to what it is decorating, proxy doesn't have to
Proxy works even when an object hasn't been initialized
