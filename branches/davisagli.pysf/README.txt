1. Check out:
svn co https://salesforce-beatbox.googlecode.com/svn/branches/davisagli.pysf davisagli.pysf

2. Patch suds:
patch -p0 < suds.patch

3. Create davisagli/pysf/sfconfig.py with username and password.

3. Run buildout:
python bootstrap.py
bin/buildout

4. Run the demo:
bin/run
