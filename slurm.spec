#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : slurm
Version  : 20.02.3.1
Release  : 7
URL      : https://github.com/SchedMD/slurm/archive/slurm-20-02-3-1/slurm-20.02.3.1.tar.gz
Source0  : https://github.com/SchedMD/slurm/archive/slurm-20-02-3-1/slurm-20.02.3.1.tar.gz
Source1  : slurm.conf
Source2  : slurmdbd.conf
Source3  : cgroup.conf
Source4  : slurm.desktop
Source5  : slurm-dirs.conf
Source6  : slurm-logrotate
Summary  : A Highly Scalable Workload Manager
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0 GPL-2.0+ OpenSSL mpich2
Requires: slurm-bin = %{version}-%{release}
Requires: slurm-config = %{version}-%{release}
Requires: slurm-data = %{version}-%{release}
Requires: slurm-lib = %{version}-%{release}
Requires: slurm-license = %{version}-%{release}
Requires: slurm-man = %{version}-%{release}
Requires: slurm-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : curl-dev
BuildRequires : dejagnu
BuildRequires : expect
BuildRequires : freeipmi-dev
BuildRequires : gettext-bin
BuildRequires : glib-dev
BuildRequires : gtk+-dev
BuildRequires : hdf5-dev
BuildRequires : hwloc-dev
BuildRequires : json-c-dev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : lua-dev
BuildRequires : lz4-dev
BuildRequires : m4
BuildRequires : mariadb-dev
BuildRequires : munge-dev
BuildRequires : ncurses-dev
BuildRequires : nghttp2-dev
BuildRequires : numactl-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(check)
BuildRequires : pmix-dev
BuildRequires : readline-dev
BuildRequires : rrdtool-dev
BuildRequires : systemd-dev
BuildRequires : tcl
BuildRequires : zlib-dev
Patch1: stateless.patch
Patch2: slurm_service_files.patch
Patch3: slurm_without_cray.patch

%description
Slurm is an open source, fault-tolerant, and highly scalable
cluster management and job scheduling system for Linux clusters.
Components include machine status, partition management,
job management, scheduling and accounting modules

%package bin
Summary: bin components for the slurm package.
Group: Binaries
Requires: slurm-data = %{version}-%{release}
Requires: slurm-config = %{version}-%{release}
Requires: slurm-license = %{version}-%{release}
Requires: slurm-services = %{version}-%{release}

%description bin
bin components for the slurm package.


%package config
Summary: config components for the slurm package.
Group: Default

%description config
config components for the slurm package.


%package data
Summary: data components for the slurm package.
Group: Data

%description data
data components for the slurm package.


%package dev
Summary: dev components for the slurm package.
Group: Development
Requires: slurm-lib = %{version}-%{release}
Requires: slurm-bin = %{version}-%{release}
Requires: slurm-data = %{version}-%{release}
Provides: slurm-devel = %{version}-%{release}
Requires: slurm = %{version}-%{release}

%description dev
dev components for the slurm package.


%package doc
Summary: doc components for the slurm package.
Group: Documentation
Requires: slurm-man = %{version}-%{release}

%description doc
doc components for the slurm package.


%package lib
Summary: lib components for the slurm package.
Group: Libraries
Requires: slurm-data = %{version}-%{release}
Requires: slurm-license = %{version}-%{release}

%description lib
lib components for the slurm package.


%package license
Summary: license components for the slurm package.
Group: Default

%description license
license components for the slurm package.


%package man
Summary: man components for the slurm package.
Group: Default

%description man
man components for the slurm package.


%package services
Summary: services components for the slurm package.
Group: Systemd services

%description services
services components for the slurm package.


%prep
%setup -q -n slurm-slurm-20-02-3-1
cd %{_builddir}/slurm-slurm-20-02-3-1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
## build_prepend content
export CFLAGS="$CFLAGS  -Wl,-z,lazy -fcommon"
export CXXFLAGS="$CXXFLAGS -Wl,-z,lazy -fcommon"
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594765972
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static --sysconfdir=/etc/slurm \
--enable-shared \
--enable-x11 \
--disable-static \
--with-pmix=/usr \
--without-rpath \
--enable-pam \
--with-pam_dir=/usr/lib64/security
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1594765972
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/slurm
cp %{_builddir}/slurm-slurm-20-02-3-1/COPYING %{buildroot}/usr/share/package-licenses/slurm/608c387fae8e4df19a3b54a0af077713eb442273
cp %{_builddir}/slurm-slurm-20-02-3-1/LICENSE.OpenSSL %{buildroot}/usr/share/package-licenses/slurm/2ae5e269080de0427f203acc42638e891c55f6db
cp %{_builddir}/slurm-slurm-20-02-3-1/contribs/pmi2/COPYRIGHT %{buildroot}/usr/share/package-licenses/slurm/6dc21c41dc6c43047082b7e4047cfb078c3b0a22
cp %{_builddir}/slurm-slurm-20-02-3-1/src/common/uthash/LICENSE %{buildroot}/usr/share/package-licenses/slurm/be83d59a077bcf54dc00639ced48a9caf4ee7ac1
%make_install
mkdir -p %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p %{_sourcedir}/slurm.conf %{buildroot}/usr/share/defaults/slurm/slurm.conf
mkdir -p %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p %{_sourcedir}/slurmdbd.conf %{buildroot}/usr/share/defaults/slurm/slurmdbd.conf
mkdir -p %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p %{_sourcedir}/cgroup.conf %{buildroot}/usr/share/defaults/slurm/cgroup.conf
mkdir -p %{buildroot}/usr/share/applications
install  %{_sourcedir}/slurm.desktop %{buildroot}/usr/share/applications/
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install  %{_sourcedir}/slurm-dirs.conf %{buildroot}/usr/lib/tmpfiles.d/slurm-dirs.conf
mkdir -p %{buildroot}/usr/share/defaults/slurm/logrotate.d
install -m 0644 -p %{_sourcedir}/slurm-logrotate %{buildroot}/usr/share/defaults/slurm/logrotate.d/slurm
## install_append content
install -Dpm 0644 ./doc/html/slurm_logo.png %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/slurm_logo.png
mkdir -p  %{buildroot}/usr/lib/systemd/system
install -m 0644 -p etc/slurmctld.service %{buildroot}/usr/lib/systemd/system
install -m 0644 -p etc/slurmd.service %{buildroot}/usr/lib/systemd/system
install -m 0644 -p etc/slurmdbd.service %{buildroot}/usr/lib/systemd/system

mkdir -p %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p etc/slurm.conf.example %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p etc/slurmdbd.conf.example %{buildroot}/usr/share/defaults/slurm
install -m 0644 -p etc/cgroup.conf.example %{buildroot}/usr/share/defaults/slurm

mkdir -p %{buildroot}/usr/share/defaults/slurm/layouts.d
install -m 0644 -p etc/layouts.d.power.conf.example %{buildroot}/usr/share/defaults/slurm/layouts.d
install -m 0644 -p etc/layouts.d.power_cpufreq.conf.example %{buildroot}/usr/share/defaults/slurm/layouts.d
install -m 0644 -p etc/layouts.d.unit.conf.example %{buildroot}/usr/share/defaults/slurm/layouts.d
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sacct
/usr/bin/sacctmgr
/usr/bin/salloc
/usr/bin/sattach
/usr/bin/sbatch
/usr/bin/sbcast
/usr/bin/scancel
/usr/bin/scontrol
/usr/bin/sdiag
/usr/bin/sh5util
/usr/bin/sinfo
/usr/bin/slurmctld
/usr/bin/slurmd
/usr/bin/slurmdbd
/usr/bin/slurmstepd
/usr/bin/sprio
/usr/bin/squeue
/usr/bin/sreport
/usr/bin/srun
/usr/bin/sshare
/usr/bin/sstat
/usr/bin/strigger
/usr/bin/sview

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/slurm-dirs.conf

%files data
%defattr(-,root,root,-)
/usr/share/applications/slurm.desktop
/usr/share/defaults/slurm/cgroup.conf
/usr/share/defaults/slurm/cgroup.conf.example
/usr/share/defaults/slurm/layouts.d/layouts.d.power.conf.example
/usr/share/defaults/slurm/layouts.d/layouts.d.power_cpufreq.conf.example
/usr/share/defaults/slurm/layouts.d/layouts.d.unit.conf.example
/usr/share/defaults/slurm/logrotate.d/slurm
/usr/share/defaults/slurm/slurm.conf
/usr/share/defaults/slurm/slurm.conf.example
/usr/share/defaults/slurm/slurmdbd.conf
/usr/share/defaults/slurm/slurmdbd.conf.example
/usr/share/icons/hicolor/scalable/apps/slurm_logo.png

%files dev
%defattr(-,root,root,-)
/usr/include/slurm/pmi.h
/usr/include/slurm/slurm.h
/usr/include/slurm/slurm_errno.h
/usr/include/slurm/slurmdb.h
/usr/include/slurm/smd_ns.h
/usr/include/slurm/spank.h
/usr/lib64/libslurm.so
/usr/lib64/slurm/src/sattach/sattach.wrapper.c
/usr/lib64/slurm/src/srun/srun.wrapper.c
/usr/share/man/man3/slurm_allocate_het_job_blocking.3
/usr/share/man/man3/slurm_allocate_resources.3
/usr/share/man/man3/slurm_allocate_resources_blocking.3
/usr/share/man/man3/slurm_allocation_lookup.3
/usr/share/man/man3/slurm_allocation_msg_thr_create.3
/usr/share/man/man3/slurm_allocation_msg_thr_destroy.3
/usr/share/man/man3/slurm_api_version.3
/usr/share/man/man3/slurm_clear_trigger.3
/usr/share/man/man3/slurm_complete_job.3
/usr/share/man/man3/slurm_confirm_allocation.3
/usr/share/man/man3/slurm_create_partition.3
/usr/share/man/man3/slurm_create_reservation.3
/usr/share/man/man3/slurm_delete_partition.3
/usr/share/man/man3/slurm_delete_reservation.3
/usr/share/man/man3/slurm_free_ctl_conf.3
/usr/share/man/man3/slurm_free_front_end_info_msg.3
/usr/share/man/man3/slurm_free_job_alloc_info_response_msg.3
/usr/share/man/man3/slurm_free_job_array_resp.3
/usr/share/man/man3/slurm_free_job_info_msg.3
/usr/share/man/man3/slurm_free_job_step_create_response_msg.3
/usr/share/man/man3/slurm_free_job_step_info_response_msg.3
/usr/share/man/man3/slurm_free_node_info.3
/usr/share/man/man3/slurm_free_node_info_msg.3
/usr/share/man/man3/slurm_free_partition_info.3
/usr/share/man/man3/slurm_free_partition_info_msg.3
/usr/share/man/man3/slurm_free_reservation_info_msg.3
/usr/share/man/man3/slurm_free_resource_allocation_response_msg.3
/usr/share/man/man3/slurm_free_slurmd_status.3
/usr/share/man/man3/slurm_free_submit_response_response_msg.3
/usr/share/man/man3/slurm_free_trigger_msg.3
/usr/share/man/man3/slurm_get_end_time.3
/usr/share/man/man3/slurm_get_errno.3
/usr/share/man/man3/slurm_get_job_steps.3
/usr/share/man/man3/slurm_get_rem_time.3
/usr/share/man/man3/slurm_get_triggers.3
/usr/share/man/man3/slurm_het_job_lookup.3
/usr/share/man/man3/slurm_het_job_will_run.3
/usr/share/man/man3/slurm_hostlist_create.3
/usr/share/man/man3/slurm_hostlist_destroy.3
/usr/share/man/man3/slurm_hostlist_shift.3
/usr/share/man/man3/slurm_init_job_desc_msg.3
/usr/share/man/man3/slurm_init_part_desc_msg.3
/usr/share/man/man3/slurm_init_resv_desc_msg.3
/usr/share/man/man3/slurm_init_trigger_msg.3
/usr/share/man/man3/slurm_init_update_front_end_msg.3
/usr/share/man/man3/slurm_init_update_node_msg.3
/usr/share/man/man3/slurm_init_update_step_msg.3
/usr/share/man/man3/slurm_job_cpus_allocated_on_node.3
/usr/share/man/man3/slurm_job_cpus_allocated_on_node_id.3
/usr/share/man/man3/slurm_job_step_create.3
/usr/share/man/man3/slurm_job_step_launch_t_init.3
/usr/share/man/man3/slurm_job_step_layout_free.3
/usr/share/man/man3/slurm_job_step_layout_get.3
/usr/share/man/man3/slurm_job_will_run.3
/usr/share/man/man3/slurm_job_will_run2.3
/usr/share/man/man3/slurm_jobinfo_ctx_get.3
/usr/share/man/man3/slurm_kill_job.3
/usr/share/man/man3/slurm_kill_job_step.3
/usr/share/man/man3/slurm_load_ctl_conf.3
/usr/share/man/man3/slurm_load_front_end.3
/usr/share/man/man3/slurm_load_job.3
/usr/share/man/man3/slurm_load_job_user.3
/usr/share/man/man3/slurm_load_jobs.3
/usr/share/man/man3/slurm_load_node.3
/usr/share/man/man3/slurm_load_node_single.3
/usr/share/man/man3/slurm_load_partitions.3
/usr/share/man/man3/slurm_load_reservations.3
/usr/share/man/man3/slurm_load_slurmd_status.3
/usr/share/man/man3/slurm_notify_job.3
/usr/share/man/man3/slurm_perror.3
/usr/share/man/man3/slurm_pid2jobid.3
/usr/share/man/man3/slurm_ping.3
/usr/share/man/man3/slurm_print_ctl_conf.3
/usr/share/man/man3/slurm_print_front_end_info_msg.3
/usr/share/man/man3/slurm_print_front_end_table.3
/usr/share/man/man3/slurm_print_job_info.3
/usr/share/man/man3/slurm_print_job_info_msg.3
/usr/share/man/man3/slurm_print_job_step_info.3
/usr/share/man/man3/slurm_print_job_step_info_msg.3
/usr/share/man/man3/slurm_print_node_info_msg.3
/usr/share/man/man3/slurm_print_node_table.3
/usr/share/man/man3/slurm_print_partition_info.3
/usr/share/man/man3/slurm_print_partition_info_msg.3
/usr/share/man/man3/slurm_print_reservation_info.3
/usr/share/man/man3/slurm_print_reservation_info_msg.3
/usr/share/man/man3/slurm_print_slurmd_status.3
/usr/share/man/man3/slurm_read_hostfile.3
/usr/share/man/man3/slurm_reconfigure.3
/usr/share/man/man3/slurm_requeue.3
/usr/share/man/man3/slurm_requeue2.3
/usr/share/man/man3/slurm_resume.3
/usr/share/man/man3/slurm_resume2.3
/usr/share/man/man3/slurm_set_debug_level.3
/usr/share/man/man3/slurm_set_trigger.3
/usr/share/man/man3/slurm_shutdown.3
/usr/share/man/man3/slurm_signal_job.3
/usr/share/man/man3/slurm_signal_job_step.3
/usr/share/man/man3/slurm_slurmd_status.3
/usr/share/man/man3/slurm_sprint_front_end_table.3
/usr/share/man/man3/slurm_sprint_job_info.3
/usr/share/man/man3/slurm_sprint_job_step_info.3
/usr/share/man/man3/slurm_sprint_node_table.3
/usr/share/man/man3/slurm_sprint_partition_info.3
/usr/share/man/man3/slurm_sprint_reservation_info.3
/usr/share/man/man3/slurm_step_ctx_create.3
/usr/share/man/man3/slurm_step_ctx_create_no_alloc.3
/usr/share/man/man3/slurm_step_ctx_daemon_per_node_hack.3
/usr/share/man/man3/slurm_step_ctx_destroy.3
/usr/share/man/man3/slurm_step_ctx_get.3
/usr/share/man/man3/slurm_step_ctx_params_t_init.3
/usr/share/man/man3/slurm_step_launch.3
/usr/share/man/man3/slurm_step_launch_abort.3
/usr/share/man/man3/slurm_step_launch_fwd_signal.3
/usr/share/man/man3/slurm_step_launch_wait_finish.3
/usr/share/man/man3/slurm_step_launch_wait_start.3
/usr/share/man/man3/slurm_strerror.3
/usr/share/man/man3/slurm_submit_batch_job.3
/usr/share/man/man3/slurm_suspend.3
/usr/share/man/man3/slurm_suspend2.3
/usr/share/man/man3/slurm_takeover.3
/usr/share/man/man3/slurm_terminate_job.3
/usr/share/man/man3/slurm_terminate_job_step.3
/usr/share/man/man3/slurm_update_front_end.3
/usr/share/man/man3/slurm_update_job.3
/usr/share/man/man3/slurm_update_job2.3
/usr/share/man/man3/slurm_update_node.3
/usr/share/man/man3/slurm_update_partition.3
/usr/share/man/man3/slurm_update_reservation.3
/usr/share/man/man3/slurm_update_step.3

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/slurm-20.02.3/html/Slurm_Entity.pdf
/usr/share/doc/slurm-20.02.3/html/Slurm_Individual.pdf
/usr/share/doc/slurm-20.02.3/html/accounting.html
/usr/share/doc/slurm-20.02.3/html/accounting_storageplugins.html
/usr/share/doc/slurm-20.02.3/html/acct_gather_energy_plugins.html
/usr/share/doc/slurm-20.02.3/html/acct_gather_profile_plugins.html
/usr/share/doc/slurm-20.02.3/html/add.html
/usr/share/doc/slurm-20.02.3/html/allocation_pies.gif
/usr/share/doc/slurm-20.02.3/html/api.html
/usr/share/doc/slurm-20.02.3/html/arch.gif
/usr/share/doc/slurm-20.02.3/html/authplugins.html
/usr/share/doc/slurm-20.02.3/html/bb_plugins.html
/usr/share/doc/slurm-20.02.3/html/big_sys.html
/usr/share/doc/slurm-20.02.3/html/burst_buffer.html
/usr/share/doc/slurm-20.02.3/html/cgroups.html
/usr/share/doc/slurm-20.02.3/html/classic_fair_share.html
/usr/share/doc/slurm-20.02.3/html/cli_filter_plugins.html
/usr/share/doc/slurm-20.02.3/html/coding_style.pdf
/usr/share/doc/slurm-20.02.3/html/configless_slurm.html
/usr/share/doc/slurm-20.02.3/html/configurator.easy.html
/usr/share/doc/slurm-20.02.3/html/configurator.html
/usr/share/doc/slurm-20.02.3/html/cons_res.html
/usr/share/doc/slurm-20.02.3/html/cons_res_share.html
/usr/share/doc/slurm-20.02.3/html/containers.html
/usr/share/doc/slurm-20.02.3/html/contributor.html
/usr/share/doc/slurm-20.02.3/html/core_spec.html
/usr/share/doc/slurm-20.02.3/html/core_spec_plugins.html
/usr/share/doc/slurm-20.02.3/html/cpu_management.html
/usr/share/doc/slurm-20.02.3/html/cray.html
/usr/share/doc/slurm-20.02.3/html/cred_plugins.html
/usr/share/doc/slurm-20.02.3/html/disclaimer.html
/usr/share/doc/slurm-20.02.3/html/dist_plane.html
/usr/share/doc/slurm-20.02.3/html/documentation.html
/usr/share/doc/slurm-20.02.3/html/download.html
/usr/share/doc/slurm-20.02.3/html/elastic_computing.html
/usr/share/doc/slurm-20.02.3/html/elasticsearch.html
/usr/share/doc/slurm-20.02.3/html/entities.gif
/usr/share/doc/slurm-20.02.3/html/example_usage.gif
/usr/share/doc/slurm-20.02.3/html/ext_sensorsplugins.html
/usr/share/doc/slurm-20.02.3/html/fair_tree.html
/usr/share/doc/slurm-20.02.3/html/faq.html
/usr/share/doc/slurm-20.02.3/html/federation.html
/usr/share/doc/slurm-20.02.3/html/fonts.css
/usr/share/doc/slurm-20.02.3/html/fonts.ttf
/usr/share/doc/slurm-20.02.3/html/gang_scheduling.html
/usr/share/doc/slurm-20.02.3/html/gres.html
/usr/share/doc/slurm-20.02.3/html/gres_design.html
/usr/share/doc/slurm-20.02.3/html/gres_plugins.html
/usr/share/doc/slurm-20.02.3/html/hdf5_job_outline.png
/usr/share/doc/slurm-20.02.3/html/hdf5_profile_user_guide.html
/usr/share/doc/slurm-20.02.3/html/hdf5_task_attr.png
/usr/share/doc/slurm-20.02.3/html/heterogeneous_jobs.html
/usr/share/doc/slurm-20.02.3/html/high_throughput.html
/usr/share/doc/slurm-20.02.3/html/ibm_pe_fig1.png
/usr/share/doc/slurm-20.02.3/html/ibm_pe_fig2.png
/usr/share/doc/slurm-20.02.3/html/intel_knl.html
/usr/share/doc/slurm-20.02.3/html/job_array.html
/usr/share/doc/slurm-20.02.3/html/job_container_plugins.html
/usr/share/doc/slurm-20.02.3/html/job_exit_code.html
/usr/share/doc/slurm-20.02.3/html/job_launch.html
/usr/share/doc/slurm-20.02.3/html/job_submit_plugins.html
/usr/share/doc/slurm-20.02.3/html/jobacct_gatherplugins.html
/usr/share/doc/slurm-20.02.3/html/jobcompplugins.html
/usr/share/doc/slurm-20.02.3/html/jquery.min.js
/usr/share/doc/slurm-20.02.3/html/jwt.html
/usr/share/doc/slurm-20.02.3/html/k_function.gif
/usr/share/doc/slurm-20.02.3/html/launch_plugins.html
/usr/share/doc/slurm-20.02.3/html/licenses.html
/usr/share/doc/slurm-20.02.3/html/mail.html
/usr/share/doc/slurm-20.02.3/html/man_index.html
/usr/share/doc/slurm-20.02.3/html/mc_support.gif
/usr/share/doc/slurm-20.02.3/html/mc_support.html
/usr/share/doc/slurm-20.02.3/html/mcs.html
/usr/share/doc/slurm-20.02.3/html/mcs_plugins.html
/usr/share/doc/slurm-20.02.3/html/meetings.html
/usr/share/doc/slurm-20.02.3/html/mpi_guide.html
/usr/share/doc/slurm-20.02.3/html/mpiplugins.html
/usr/share/doc/slurm-20.02.3/html/multi_cluster.html
/usr/share/doc/slurm-20.02.3/html/news.html
/usr/share/doc/slurm-20.02.3/html/node_features_plugins.html
/usr/share/doc/slurm-20.02.3/html/nss_slurm.html
/usr/share/doc/slurm-20.02.3/html/overview.html
/usr/share/doc/slurm-20.02.3/html/pam_slurm_adopt.html
/usr/share/doc/slurm-20.02.3/html/plane_ex1.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex2.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex3.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex4.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex5.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex6.gif
/usr/share/doc/slurm-20.02.3/html/plane_ex7.gif
/usr/share/doc/slurm-20.02.3/html/platforms.html
/usr/share/doc/slurm-20.02.3/html/plugins.html
/usr/share/doc/slurm-20.02.3/html/power_mgmt.html
/usr/share/doc/slurm-20.02.3/html/power_plugins.html
/usr/share/doc/slurm-20.02.3/html/power_save.html
/usr/share/doc/slurm-20.02.3/html/preempt.html
/usr/share/doc/slurm-20.02.3/html/preemption_plugins.html
/usr/share/doc/slurm-20.02.3/html/prep_plugins.html
/usr/share/doc/slurm-20.02.3/html/priority_multifactor.html
/usr/share/doc/slurm-20.02.3/html/priority_multifactor3.html
/usr/share/doc/slurm-20.02.3/html/priority_plugins.html
/usr/share/doc/slurm-20.02.3/html/proctrack_plugins.html
/usr/share/doc/slurm-20.02.3/html/programmer_guide.html
/usr/share/doc/slurm-20.02.3/html/prolog_epilog.html
/usr/share/doc/slurm-20.02.3/html/publications.html
/usr/share/doc/slurm-20.02.3/html/qos.html
/usr/share/doc/slurm-20.02.3/html/quickstart.html
/usr/share/doc/slurm-20.02.3/html/quickstart_admin.html
/usr/share/doc/slurm-20.02.3/html/reservations.html
/usr/share/doc/slurm-20.02.3/html/reset.css
/usr/share/doc/slurm-20.02.3/html/resource_binding.html
/usr/share/doc/slurm-20.02.3/html/resource_limits.html
/usr/share/doc/slurm-20.02.3/html/rest.html
/usr/share/doc/slurm-20.02.3/html/rosetta.html
/usr/share/doc/slurm-20.02.3/html/route_plugin.html
/usr/share/doc/slurm-20.02.3/html/sched_config.html
/usr/share/doc/slurm-20.02.3/html/schedmd.png
/usr/share/doc/slurm-20.02.3/html/schedplugins.html
/usr/share/doc/slurm-20.02.3/html/select_design.html
/usr/share/doc/slurm-20.02.3/html/selectplugins.html
/usr/share/doc/slurm-20.02.3/html/site_factor.html
/usr/share/doc/slurm-20.02.3/html/slurm.css
/usr/share/doc/slurm-20.02.3/html/slurm.html
/usr/share/doc/slurm-20.02.3/html/slurm_logo.png
/usr/share/doc/slurm-20.02.3/html/slurm_ug_agenda.html
/usr/share/doc/slurm-20.02.3/html/slurmctld_plugstack.html
/usr/share/doc/slurm-20.02.3/html/squeue_color.png
/usr/share/doc/slurm-20.02.3/html/style.css
/usr/share/doc/slurm-20.02.3/html/switchplugins.html
/usr/share/doc/slurm-20.02.3/html/taskplugins.html
/usr/share/doc/slurm-20.02.3/html/team.html
/usr/share/doc/slurm-20.02.3/html/testimonials.html
/usr/share/doc/slurm-20.02.3/html/topo_ex1.gif
/usr/share/doc/slurm-20.02.3/html/topo_ex2.gif
/usr/share/doc/slurm-20.02.3/html/topology.html
/usr/share/doc/slurm-20.02.3/html/topology_plugin.html
/usr/share/doc/slurm-20.02.3/html/tres.html
/usr/share/doc/slurm-20.02.3/html/troubleshoot.html
/usr/share/doc/slurm-20.02.3/html/tutorial_intro_files.tar
/usr/share/doc/slurm-20.02.3/html/tutorials.html
/usr/share/doc/slurm-20.02.3/html/usage_pies.gif
/usr/share/doc/slurm-20.02.3/html/user_permissions.html
/usr/share/doc/slurm-20.02.3/html/wckey.html

%files lib
%defattr(-,root,root,-)
/usr/lib64/libslurm.so.35
/usr/lib64/libslurm.so.35.0.0
/usr/lib64/slurm/accounting_storage_filetxt.so
/usr/lib64/slurm/accounting_storage_mysql.so
/usr/lib64/slurm/accounting_storage_none.so
/usr/lib64/slurm/accounting_storage_slurmdbd.so
/usr/lib64/slurm/acct_gather_energy_ibmaem.so
/usr/lib64/slurm/acct_gather_energy_ipmi.so
/usr/lib64/slurm/acct_gather_energy_none.so
/usr/lib64/slurm/acct_gather_energy_rapl.so
/usr/lib64/slurm/acct_gather_energy_xcc.so
/usr/lib64/slurm/acct_gather_filesystem_lustre.so
/usr/lib64/slurm/acct_gather_filesystem_none.so
/usr/lib64/slurm/acct_gather_interconnect_none.so
/usr/lib64/slurm/acct_gather_profile_hdf5.so
/usr/lib64/slurm/acct_gather_profile_influxdb.so
/usr/lib64/slurm/acct_gather_profile_none.so
/usr/lib64/slurm/auth_munge.so
/usr/lib64/slurm/auth_none.so
/usr/lib64/slurm/burst_buffer_datawarp.so
/usr/lib64/slurm/burst_buffer_generic.so
/usr/lib64/slurm/cli_filter_lua.so
/usr/lib64/slurm/cli_filter_none.so
/usr/lib64/slurm/cli_filter_syslog.so
/usr/lib64/slurm/cli_filter_user_defaults.so
/usr/lib64/slurm/core_spec_none.so
/usr/lib64/slurm/cred_munge.so
/usr/lib64/slurm/cred_none.so
/usr/lib64/slurm/ext_sensors_none.so
/usr/lib64/slurm/ext_sensors_rrd.so
/usr/lib64/slurm/gpu_generic.so
/usr/lib64/slurm/gres_gpu.so
/usr/lib64/slurm/gres_mic.so
/usr/lib64/slurm/gres_mps.so
/usr/lib64/slurm/gres_nic.so
/usr/lib64/slurm/job_container_none.so
/usr/lib64/slurm/job_submit_all_partitions.so
/usr/lib64/slurm/job_submit_defaults.so
/usr/lib64/slurm/job_submit_logging.so
/usr/lib64/slurm/job_submit_lua.so
/usr/lib64/slurm/job_submit_partition.so
/usr/lib64/slurm/job_submit_pbs.so
/usr/lib64/slurm/job_submit_require_timelimit.so
/usr/lib64/slurm/job_submit_throttle.so
/usr/lib64/slurm/jobacct_gather_cgroup.so
/usr/lib64/slurm/jobacct_gather_linux.so
/usr/lib64/slurm/jobacct_gather_none.so
/usr/lib64/slurm/jobcomp_elasticsearch.so
/usr/lib64/slurm/jobcomp_filetxt.so
/usr/lib64/slurm/jobcomp_lua.so
/usr/lib64/slurm/jobcomp_mysql.so
/usr/lib64/slurm/jobcomp_none.so
/usr/lib64/slurm/jobcomp_script.so
/usr/lib64/slurm/launch_slurm.so
/usr/lib64/slurm/layouts_power_cpufreq.so
/usr/lib64/slurm/layouts_power_default.so
/usr/lib64/slurm/layouts_unit_default.so
/usr/lib64/slurm/libslurmfull.so
/usr/lib64/slurm/mcs_account.so
/usr/lib64/slurm/mcs_group.so
/usr/lib64/slurm/mcs_none.so
/usr/lib64/slurm/mcs_user.so
/usr/lib64/slurm/mpi_cray_shasta.so
/usr/lib64/slurm/mpi_none.so
/usr/lib64/slurm/mpi_pmi2.so
/usr/lib64/slurm/mpi_pmix.so
/usr/lib64/slurm/mpi_pmix_v3.so
/usr/lib64/slurm/node_features_knl_generic.so
/usr/lib64/slurm/power_none.so
/usr/lib64/slurm/preempt_none.so
/usr/lib64/slurm/preempt_partition_prio.so
/usr/lib64/slurm/preempt_qos.so
/usr/lib64/slurm/prep_script.so
/usr/lib64/slurm/priority_basic.so
/usr/lib64/slurm/priority_multifactor.so
/usr/lib64/slurm/proctrack_cgroup.so
/usr/lib64/slurm/proctrack_linuxproc.so
/usr/lib64/slurm/proctrack_pgid.so
/usr/lib64/slurm/route_default.so
/usr/lib64/slurm/route_topology.so
/usr/lib64/slurm/sched_backfill.so
/usr/lib64/slurm/sched_builtin.so
/usr/lib64/slurm/sched_hold.so
/usr/lib64/slurm/select_cons_res.so
/usr/lib64/slurm/select_cons_tres.so
/usr/lib64/slurm/select_linear.so
/usr/lib64/slurm/site_factor_none.so
/usr/lib64/slurm/slurmctld_nonstop.so
/usr/lib64/slurm/spank_pbs.so
/usr/lib64/slurm/switch_generic.so
/usr/lib64/slurm/switch_none.so
/usr/lib64/slurm/task_affinity.so
/usr/lib64/slurm/task_cgroup.so
/usr/lib64/slurm/task_none.so
/usr/lib64/slurm/topology_3d_torus.so
/usr/lib64/slurm/topology_hypercube.so
/usr/lib64/slurm/topology_node_rank.so
/usr/lib64/slurm/topology_none.so
/usr/lib64/slurm/topology_tree.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/slurm/2ae5e269080de0427f203acc42638e891c55f6db
/usr/share/package-licenses/slurm/608c387fae8e4df19a3b54a0af077713eb442273
/usr/share/package-licenses/slurm/6dc21c41dc6c43047082b7e4047cfb078c3b0a22
/usr/share/package-licenses/slurm/be83d59a077bcf54dc00639ced48a9caf4ee7ac1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sacct.1
/usr/share/man/man1/sacctmgr.1
/usr/share/man/man1/salloc.1
/usr/share/man/man1/sattach.1
/usr/share/man/man1/sbatch.1
/usr/share/man/man1/sbcast.1
/usr/share/man/man1/scancel.1
/usr/share/man/man1/scontrol.1
/usr/share/man/man1/sdiag.1
/usr/share/man/man1/sh5util.1
/usr/share/man/man1/sinfo.1
/usr/share/man/man1/slurm.1
/usr/share/man/man1/sprio.1
/usr/share/man/man1/squeue.1
/usr/share/man/man1/sreport.1
/usr/share/man/man1/srun.1
/usr/share/man/man1/sshare.1
/usr/share/man/man1/sstat.1
/usr/share/man/man1/strigger.1
/usr/share/man/man1/sview.1
/usr/share/man/man5/acct_gather.conf.5
/usr/share/man/man5/burst_buffer.conf.5
/usr/share/man/man5/cgroup.conf.5
/usr/share/man/man5/ext_sensors.conf.5
/usr/share/man/man5/gres.conf.5
/usr/share/man/man5/knl.conf.5
/usr/share/man/man5/nonstop.conf.5
/usr/share/man/man5/slurm.conf.5
/usr/share/man/man5/slurmdbd.conf.5
/usr/share/man/man5/topology.conf.5
/usr/share/man/man8/slurmctld.8
/usr/share/man/man8/slurmd.8
/usr/share/man/man8/slurmdbd.8
/usr/share/man/man8/slurmrestd.8
/usr/share/man/man8/slurmstepd.8
/usr/share/man/man8/spank.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/slurmctld.service
/usr/lib/systemd/system/slurmd.service
/usr/lib/systemd/system/slurmdbd.service
