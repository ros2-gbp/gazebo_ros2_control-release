%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-gazebo-ros2-control
Version:        0.4.10
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS gazebo_ros2_control package

License:        BSD and Apache License 2.0
URL:            http://ros.org/wiki/gazebo_ros_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-angles
Requires:       ros-humble-control-toolbox
Requires:       ros-humble-controller-manager
Requires:       ros-humble-gazebo-dev
Requires:       ros-humble-gazebo-ros
Requires:       ros-humble-hardware-interface
Requires:       ros-humble-pluginlib
Requires:       ros-humble-rclcpp
Requires:       ros-humble-std-msgs
Requires:       ros-humble-yaml-cpp-vendor
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake
BuildRequires:  ros-humble-angles
BuildRequires:  ros-humble-control-toolbox
BuildRequires:  ros-humble-controller-manager
BuildRequires:  ros-humble-gazebo-dev
BuildRequires:  ros-humble-gazebo-ros
BuildRequires:  ros-humble-hardware-interface
BuildRequires:  ros-humble-pluginlib
BuildRequires:  ros-humble-rclcpp
BuildRequires:  ros-humble-std-msgs
BuildRequires:  ros-humble-yaml-cpp-vendor
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-cmake-gtest
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%description
gazebo_ros2_control

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Tue Sep 17 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.10-1
- Autogenerated by Bloom

* Tue Jul 02 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.9-1
- Autogenerated by Bloom

* Tue May 14 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.8-1
- Autogenerated by Bloom

* Thu Mar 21 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.7-1
- Autogenerated by Bloom

* Wed Jan 24 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.6-1
- Autogenerated by Bloom

* Thu Jan 04 2024 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.5-1
- Autogenerated by Bloom

* Tue Aug 22 2023 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.4-1
- Autogenerated by Bloom

* Tue May 23 2023 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.3-1
- Autogenerated by Bloom

* Thu Mar 02 2023 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.2-1
- Autogenerated by Bloom

* Tue Feb 07 2023 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.5.0-1
- Autogenerated by Bloom

* Tue Feb 07 2023 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.1-1
- Autogenerated by Bloom

* Tue Aug 09 2022 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.4.0-1
- Autogenerated by Bloom

* Fri May 27 2022 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.3.0-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.0.8-3
- Autogenerated by Bloom

* Wed Feb 23 2022 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.0.8-2
- Autogenerated by Bloom

* Fri Jan 28 2022 Alejandro Hernandez <alejandro@osrfoundation.org> - 0.0.8-1
- Autogenerated by Bloom

