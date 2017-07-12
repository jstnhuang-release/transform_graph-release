Name:           ros-indigo-transform-graph
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS transform_graph package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://wiki.ros.org/transform_graph
Source0:        %{name}-%{version}.tar.gz

Requires:       pcl
Requires:       pcl-tools
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-tf
BuildRequires:  pcl
BuildRequires:  pcl-tools
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rosunit
BuildRequires:  ros-indigo-tf

%description
Library for computing transformations in arbitrary graph structures.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Jul 12 2017 Justin Huang <jstn@cs.washington.edu> - 0.2.0-0
- Autogenerated by Bloom

* Fri May 26 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.4-0
- Autogenerated by Bloom

* Thu May 25 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.3-0
- Autogenerated by Bloom

* Wed May 24 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.2-0
- Autogenerated by Bloom

* Fri May 05 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.1-0
- Autogenerated by Bloom

* Wed May 03 2017 Justin Huang <jstn@cs.washington.edu> - 0.1.0-0
- Autogenerated by Bloom

