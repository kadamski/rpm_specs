srpm:
	mkdir -p rpmbuild/SOURCES
	rpmbuild --undefine=_disable_source_fetch -D'_srcrpmdir $(outdir)' -bs $(spec) 
