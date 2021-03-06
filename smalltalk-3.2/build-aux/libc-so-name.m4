# libc-so-name.m4 serial 1
dnl Copyright (C) 2003, 2009 Free Software Foundation, Inc.
dnl This file is free software, distributed under the terms of the GNU
dnl General Public License.  As a special exception to the GNU General
dnl Public License, this file may be distributed as part of a program
dnl that contains a configuration script generated by Autoconf, under
dnl the same distribution terms as the rest of that program.

dnl Sets the variables LIBC_SO_NAME and LIBC_SO_DIR to the directory
dnl and basename for the C library.
AC_DEFUN([GST_LIBC_SO_NAME],
[AC_CACHE_CHECK([how to dlopen the C library], gst_cv_libc_so_name, [
  if test $GCC = yes; then
    gst_lib_path=`$CC --print-multi-os-directory $CFLAGS $CPPFLAGS`
    case $gst_lib_path in
      .) gst_lib_path= ;;
      *) gst_lib_path=$gst_lib_path/ ;;
    esac
  else
    gst_lib_path=
  fi
  case $gst_lib_path in
    /*) gst_libc_search_path="${gst_lib_path}libc.so*
	  ${gst_lib_path}libc-*.so
	  ${gst_lib_path}libc.sl
	  ${gst_lib_path}libSystem.dylib" ;;
    *) gst_libc_search_path="/shlib/libc.so \
	/lib/${gst_lib_path}libc.so* \
	/usr/lib/${gst_lib_path}libc.so.* \
	/usr/lib/${gst_lib_path}libc.sl \
	/lib/${gst_lib_path}libc-*.so \
	/System/Library/Frameworks/System.framework/System \
	/usr/lib/libSystem.dylib"
  esac

  gst_lib_sysroot=`$CC --print-sysroot`
  for i in $gst_libc_search_path; do
    if test -f "$gst_lib_sysroot$i"; then
      oldwd=`pwd`
      gst_cv_libc_so_name=`basename $i`
      gst_cv_libc_so_dir=`dirname $i`
      cd "$gst_cv_libc_so_dir" && gst_cv_libc_so_dir=`pwd`
      cd $oldwd
      break
    fi
  done])
LIBC_SO_NAME=$gst_cv_libc_so_name
LIBC_SO_DIR=$gst_cv_libc_so_dir
AC_SUBST(LIBC_SO_NAME)
AC_SUBST(LIBC_SO_DIR)
])
