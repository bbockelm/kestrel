# kestrel
OSG tools for interacting with glideinWMS

Kestrel is a set of tools to improve interactions with the glideinWMS software suite.

## Usage

Kestrel is a set of tools for interacting with glideinWMS.  This section provides an overview of how to use each tool.

### gfactory_entry_requests

The `gfactory_entry_requests` prints out a line per-frontend, per-group, per-entry of the requests made to the given factory.
It is a wrapper around the venerable `condor_status` client and inherits its command line options.  For example, you can
use the `-const` option to filter information.  To look only at requests from the `CMSG-v1_0` frontend, you can do:

```
$ gfactory_entry_requests -const 'FrontendName=?="CMSG-v1_0"'
```

### gfactory_frontend_info

The `gfactory_frontend_info` discovers all known frontends that are connected to a factory.  It prints out the
frontend name, the frontend's VO collector, identity, collector HTCondor version, and monitoring URL.  The
tool is oriented toward assisting operators in discovering useful frontend information for debugging.

### gfactory_frontend_groups

Print out all frontends and groups registered with a given factory.

### gwms_analyze_job

Given a VO collector name, schedd, and job ID, print out any matching sites or entry points.

If there are no matching sites, summarize the reason why each site was excluded.

An example invocation:

```
gwms_analyze_job -p collector.example.com -n schedd.example.com 1880275.0 --unsafe
```

*Note*: this script must run arbitrary python code controlled by the frontend.  Only use it if this is an acceptable situation.

## INSTALLATION

To install Kestrel, run:

```
python setup.py sdist && cp dist/*.tar.gz ~/rpmbuild/SOURCES
rpmbuild -ba config/kestrel.spec
rpm -Uhv ~/rpmbuild/RPMS/noarch/kestrel-*.rpm
``` 
