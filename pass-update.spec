Name:           pass-update
Version:        2.1
Release:        1%{?dist}
Summary:        A pass extension that provides an easy flow for updating passwords.
BuildArch:      noarch

License:        GPLv3
URL:            https://github.com/roddhjav/%{name}
Source0:        https://github.com/roddhjav/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Requires:       bash pass

%description
pass update extends the pass utility with an update command providing an easy
flow for updating passwords. It supports path, directory and wildcard update.
Moreover, you can select how to update your passwords by automatically
generating new passwords or manually setting your own.

pass update assumes that the first line of the password file is the password
and so only ever updates the first line unless the --multiline option is
specified.

%prep
%setup -q

%build

%install
%make_install

%files
%license LICENSE
%{_sysconfdir}/bash_completion.d/%{name}
%{_prefix}/lib/password-store/extensions/update.bash
%{_datarootdir}/zsh/site-functions/_%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
* Thu Feb 14 2019 Krzysztof Adamski <k@japko.eu>
- Initial version
