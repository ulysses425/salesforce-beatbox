1. Check out:
svn co https://salesforce-beatbox.googlecode.com/svn/branches/davisagli.pysf davisagli.pysf

2. Patch suds:
patch -p0 < suds.patch

3. Run buildout:
python bootstrap.py
bin/buildout

4. Create davisagli/pysf/sfconfig.py with username and password.

5. Update path to WSDL in davisagli/pysf/main.py.

6. Run the demo:
bin/run
