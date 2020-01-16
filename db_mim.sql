-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 13, 2020 at 04:48 PM
-- Server version: 10.4.6-MariaDB
-- PHP Version: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_mim`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_group`
--

INSERT INTO `auth_group` (`id`, `name`) VALUES
(1, 'students'),
(2, 'teachers');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add guru', 7, 'add_guru'),
(20, 'Can change guru', 7, 'change_guru'),
(21, 'Can delete guru', 7, 'delete_guru'),
(22, 'Can add hari', 8, 'add_hari'),
(23, 'Can change hari', 8, 'change_hari'),
(24, 'Can delete hari', 8, 'delete_hari'),
(25, 'Can add kelas', 9, 'add_kelas'),
(26, 'Can change kelas', 9, 'change_kelas'),
(27, 'Can delete kelas', 9, 'delete_kelas'),
(28, 'Can add mapel', 10, 'add_mapel'),
(29, 'Can change mapel', 10, 'change_mapel'),
(30, 'Can delete mapel', 10, 'delete_mapel'),
(31, 'Can add penjadwalan', 11, 'add_penjadwalan'),
(32, 'Can change penjadwalan', 11, 'change_penjadwalan'),
(33, 'Can delete penjadwalan', 11, 'delete_penjadwalan'),
(34, 'Can add siswa', 12, 'add_siswa'),
(35, 'Can change siswa', 12, 'change_siswa'),
(36, 'Can delete siswa', 12, 'delete_siswa'),
(37, 'Can add surat_ijin', 13, 'add_surat_ijin'),
(38, 'Can change surat_ijin', 13, 'change_surat_ijin'),
(39, 'Can delete surat_ijin', 13, 'delete_surat_ijin'),
(40, 'Can add pengumuman', 14, 'add_pengumuman'),
(41, 'Can change pengumuman', 14, 'change_pengumuman'),
(42, 'Can delete pengumuman', 14, 'delete_pengumuman');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$EluioeSMBglx$ELHqieQqw2a5rRTsuVVFLSCi40MQPJeyut9L0Nv8+uI=', '2020-01-13 07:27:55.580603', 1, 'selvia', '', '', '', 1, 1, '2020-01-10 06:53:21.899176'),
(2, 'pbkdf2_sha256$100000$Xg7YMq82gsWU$opne+5YRM226ueG2gBKn4BGMV1IPdzvuSIo8kBOEE1E=', '2020-01-10 12:27:33.184235', 0, 'guru1', '', '', '', 0, 1, '2020-01-10 11:36:42.503831'),
(3, 'pbkdf2_sha256$100000$oq05LMblWkUp$BQyuqT11IgpBKKZHRUM4eDnLMGexmgpUa22JJDrgEec=', '2020-01-13 06:33:11.234486', 0, 'guru2', '', '', '', 0, 1, '2020-01-10 11:56:15.371907'),
(4, 'pbkdf2_sha256$100000$lXINYQbOlqvr$8GLwQB6NYcPIFI2CHp3E5ebA1MpoHjlNYOB5IlZv+0Y=', '2020-01-13 06:34:17.325423', 0, 'siswa1', '', '', '', 0, 1, '2020-01-10 12:08:15.059096'),
(5, 'pbkdf2_sha256$100000$YrcYcx2lunZg$ctFxbIlr5LtY7SgwdyX4cCAtGq8yZKdhJG3hFGYOayA=', NULL, 0, 'guru3', '', '', '', 0, 1, '2020-01-11 11:51:32.669999'),
(6, 'pbkdf2_sha256$100000$TkkvEDOzjU9D$z7oQpZWgRLtf1CJvI3DCcT3UeCyTjM1er06vPghAx0c=', NULL, 0, 'selpong', '', '', '', 0, 1, '2020-01-12 06:01:12.788920');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user_groups`
--

INSERT INTO `auth_user_groups` (`id`, `user_id`, `group_id`) VALUES
(1, 3, 2),
(2, 4, 1),
(3, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-01-10 06:57:14.610735', '1', 'Pengajian Rutin Ahad Pagi', 1, '[{\"added\": {}}]', 14, 1),
(2, '2020-01-10 07:06:07.488224', '1', 'selvia Ijin sakit', 1, '[{\"added\": {}}]', 13, 1),
(3, '2020-01-10 07:54:22.433060', '2', 'selvia Pengajian Rutin Ahad Pagi', 1, '[{\"added\": {}}]', 13, 1),
(4, '2020-01-10 11:05:58.336086', '2', 'selvia Pengajian Rutin Ahad Pagi', 3, '', 13, 1),
(5, '2020-01-10 11:06:12.542687', '1', 'Pengajian Rutin Ahad Pagi', 3, '', 14, 1),
(6, '2020-01-10 11:11:30.979104', '3', 'selvia Pengajian Rutin Ahad Pagi', 1, '[{\"added\": {}}]', 13, 1),
(7, '2020-01-10 11:21:41.438900', '3', 'Baitul Arqom Kepala Sekolah dan Ortom Muhammadiyah', 1, '[{\"added\": {}}]', 14, 1),
(8, '2020-01-10 11:29:27.447650', '4', 'Pengajian Rutin Ahad Pagi', 1, '[{\"added\": {}}]', 14, 1),
(9, '2020-01-10 11:32:33.287561', '4', 'selvia Ijin sakit', 1, '[{\"added\": {}}]', 13, 1),
(10, '2020-01-10 11:55:41.835211', '1', 'students', 1, '[{\"added\": {}}]', 3, 1),
(11, '2020-01-10 11:55:59.419298', '2', 'teachers', 1, '[{\"added\": {}}]', 3, 1),
(12, '2020-01-10 11:57:31.198092', '4', 'Pengajian Rutin Ahad Pagi', 2, '[{\"changed\": {\"fields\": [\"penerima\"]}}]', 14, 1),
(13, '2020-01-10 11:57:39.757026', '2', 'Pengajian Rutin Ahad Pagi', 2, '[{\"changed\": {\"fields\": [\"penerima\"]}}]', 14, 1),
(14, '2020-01-10 12:07:48.392895', '1', '1A', 1, '[{\"added\": {}}]', 9, 1),
(15, '2020-01-11 05:17:21.409489', '7', 'ppppppppp Ijin sakit', 1, '[{\"added\": {}}]', 13, 1),
(16, '2020-01-11 08:00:13.364829', '1', 'Matematika', 1, '[{\"added\": {}}]', 10, 1),
(17, '2020-01-11 08:00:15.292930', '1', 'Wahyu Cintya | Matematika', 1, '[{\"added\": {}}]', 11, 1),
(18, '2020-01-11 08:23:29.212923', '3', 'Wahyu Cintya | Matematika', 3, '', 11, 1),
(19, '2020-01-11 08:23:29.273940', '2', 'Wahyu Cintya | Matematika', 3, '', 11, 1),
(20, '2020-01-11 08:23:29.326757', '1', 'Wahyu Cintya | Matematika', 3, '', 11, 1),
(21, '2020-01-11 08:36:58.539621', '5', 'Wahyu Cintya | Matematika', 3, '', 11, 1),
(22, '2020-01-11 11:51:14.435913', '2', 'Rahayuning Putri', 1, '[{\"added\": {}}]', 7, 1),
(23, '2020-01-11 11:51:32.978080', '5', 'guru3', 1, '[{\"added\": {}}]', 4, 1),
(24, '2020-01-11 11:51:47.236198', '3', 'Selvia Tunjungsih Wahyu', 1, '[{\"added\": {}}]', 7, 1),
(25, '2020-01-11 11:52:26.059653', '2', 'Bahasa Inggris', 1, '[{\"added\": {}}]', 10, 1),
(26, '2020-01-11 11:52:35.247953', '3', 'Bahasa Indonesia', 1, '[{\"added\": {}}]', 10, 1),
(27, '2020-01-11 11:53:00.456244', '3', '3A', 1, '[{\"added\": {}}]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'penjadwalan', 'guru'),
(8, 'penjadwalan', 'hari'),
(9, 'penjadwalan', 'kelas'),
(10, 'penjadwalan', 'mapel'),
(14, 'penjadwalan', 'pengumuman'),
(11, 'penjadwalan', 'penjadwalan'),
(12, 'penjadwalan', 'siswa'),
(13, 'penjadwalan', 'surat_ijin'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-01-10 06:51:53.190764'),
(2, 'auth', '0001_initial', '2020-01-10 06:52:15.319928'),
(3, 'admin', '0001_initial', '2020-01-10 06:52:19.239689'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-01-10 06:52:19.441582'),
(5, 'contenttypes', '0002_remove_content_type_name', '2020-01-10 06:52:21.381627'),
(6, 'auth', '0002_alter_permission_name_max_length', '2020-01-10 06:52:21.588607'),
(7, 'auth', '0003_alter_user_email_max_length', '2020-01-10 06:52:21.863731'),
(8, 'auth', '0004_alter_user_username_opts', '2020-01-10 06:52:22.100783'),
(9, 'auth', '0005_alter_user_last_login_null', '2020-01-10 06:52:23.129875'),
(10, 'auth', '0006_require_contenttypes_0002', '2020-01-10 06:52:23.200646'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2020-01-10 06:52:23.265695'),
(12, 'auth', '0008_alter_user_username_max_length', '2020-01-10 06:52:25.395876'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2020-01-10 06:52:25.773113'),
(14, 'penjadwalan', '0001_initial', '2020-01-10 06:52:42.252999'),
(15, 'penjadwalan', '0002_auto_20200107_0829', '2020-01-10 06:52:45.295327'),
(16, 'penjadwalan', '0003_auto_20200107_0855', '2020-01-10 06:52:50.097105'),
(17, 'penjadwalan', '0004_auto_20200107_2141', '2020-01-10 06:52:52.884895'),
(18, 'penjadwalan', '0005_pengumuman_surat_ijin', '2020-01-10 06:52:56.131394'),
(19, 'penjadwalan', '0006_delete_pengumuman', '2020-01-10 06:52:56.551600'),
(20, 'penjadwalan', '0007_pengumuman', '2020-01-10 06:52:57.205154'),
(21, 'sessions', '0001_initial', '2020-01-10 06:52:58.536020'),
(22, 'penjadwalan', '0008_auto_20200110_1356', '2020-01-10 06:56:28.040669'),
(23, 'penjadwalan', '0009_surat_ijin_dokumen', '2020-01-10 07:05:10.376552'),
(24, 'penjadwalan', '0010_auto_20200110_1814', '2020-01-10 11:14:10.852151'),
(25, 'penjadwalan', '0011_auto_20200110_1828', '2020-01-10 11:28:50.355569'),
(26, 'penjadwalan', '0012_auto_20200110_1830', '2020-01-10 11:30:35.668920'),
(27, 'penjadwalan', '0013_auto_20200110_1831', '2020-01-10 11:31:31.350592'),
(28, 'penjadwalan', '0014_auto_20200111_1049', '2020-01-11 03:49:16.705295');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('1li40fh4gvxy7d0twflr3x3n9ewfqiru', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 06:01:13.583375'),
('ceq1rxlcki1hbb29qq9myeupu2k8u1x1', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-25 04:22:03.633450'),
('fefulwokdtk985tg4aen3arf0apblj2d', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 03:48:16.252295'),
('he6wemgo0wwnt0vjo70fequ6m73ae1qc', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 03:56:38.010127'),
('ip906gh7em5jeygdyf5cbe9hn65d224b', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-27 07:27:55.640581'),
('p6tufmyflpoluf5uaawo58o2dch5j13r', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 03:58:55.876734'),
('szcgjj3mhgskvz87lratrot2elzbazce', 'ODYxMjA4Y2RkN2YxN2ZkYWJhY2Y3YWZlNDhhZGIwMzA4NzI3MDNjMTp7Il9hdXRoX3VzZXJfaWQiOiIzIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJhNGE3NWQwNjYzYzkwZGNjYzRmYTU2OWUyNWIyZDgxOTMyYWUyYWMzIn0=', '2020-01-25 01:46:53.528889'),
('xwvh0981w9d9wjdk8u42hamgducn4qmj', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 13:57:58.980164'),
('zmhvududsuej4sx8aoka8vs85w0cbn9b', 'YmIxOTQxMzViYWQ4ZDAwMzAxNTA0NDVhZmE4YTViMzA4OGM5ZDVmNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI2MTM2YWFlZWFlMjM0MTBmZmFlZTY3Zjg4NDQ3ODcxYTg3ZDk5OWNkIn0=', '2020-01-26 14:00:37.167471');

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_guru`
--

CREATE TABLE `penjadwalan_guru` (
  `id` int(11) NOT NULL,
  `nik` varchar(15) NOT NULL,
  `kode` varchar(4) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nama_blkg` varchar(50) NOT NULL,
  `gelar` varchar(10) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_guru`
--

INSERT INTO `penjadwalan_guru` (`id`, `nik`, `kode`, `nama`, `nama_blkg`, `gelar`, `user_id`) VALUES
(1, '123', 'A', 'Wahyu', 'Dewi', 'S.Kom', 3),
(2, '1234', 'B', 'Putri', 'Mahardikawati', 'S.Pd', 2),
(3, '3456', 'C', 'Selvia', 'Kesumastuti', 'S.Kom', 5);

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_hari`
--

CREATE TABLE `penjadwalan_hari` (
  `id` int(11) NOT NULL,
  `kode_hari` varchar(10) NOT NULL,
  `hari` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_kelas`
--

CREATE TABLE `penjadwalan_kelas` (
  `id` int(11) NOT NULL,
  `kode_kelas` varchar(10) NOT NULL,
  `kelas` varchar(10) NOT NULL,
  `kapasitas` int(11) NOT NULL,
  `keterangan` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_kelas`
--

INSERT INTO `penjadwalan_kelas` (`id`, `kode_kelas`, `kelas`, `kapasitas`, `keterangan`) VALUES
(1, '1a', '1A', 32, '-'),
(2, '2a', '2A', 32, '-'),
(3, '3a', '3A', 32, '-'),
(4, '4a', '4a', 28, '-');

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_mapel`
--

CREATE TABLE `penjadwalan_mapel` (
  `id` int(11) NOT NULL,
  `kode_mapel` varchar(10) NOT NULL,
  `nama` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_mapel`
--

INSERT INTO `penjadwalan_mapel` (`id`, `kode_mapel`, `nama`) VALUES
(1, 'MAT', 'Matematika'),
(2, 'ING', 'Bahasa Inggris'),
(3, 'IND', 'Bahasa Indonesia');

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_pengumuman`
--

CREATE TABLE `penjadwalan_pengumuman` (
  `id` int(11) NOT NULL,
  `penerima` int(10) UNSIGNED NOT NULL,
  `judul` varchar(200) NOT NULL,
  `isi` longtext NOT NULL,
  `tgl_post` datetime(6) NOT NULL,
  `dokumen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_pengumuman`
--

INSERT INTO `penjadwalan_pengumuman` (`id`, `penerima`, `judul`, `isi`, `tgl_post`, `dokumen`) VALUES
(2, 2, 'Pengajian Rutin Ahad Pagi', 'hai ini di \r\n\r\n\r\nnamaku\r\nselvis', '2020-01-10 11:16:27.000000', 'pic_folder/None/no-img.jpg'),
(3, 1, 'Baitul Arqom Kepala Sekolah dan Ortom Muhammadiyah', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', '2020-01-10 11:21:08.000000', 'static/doc_pengumuman/dasbor.PNG');

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_penjadwalan`
--

CREATE TABLE `penjadwalan_penjadwalan` (
  `id` int(11) NOT NULL,
  `kode_jadwal` varchar(10) NOT NULL,
  `hari` int(10) UNSIGNED NOT NULL,
  `jamke` int(10) UNSIGNED NOT NULL,
  `guru_id` int(11) NOT NULL,
  `kelas_id` int(11) NOT NULL,
  `mapel_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_penjadwalan`
--

INSERT INTO `penjadwalan_penjadwalan` (`id`, `kode_jadwal`, `hari`, `jamke`, `guru_id`, `kelas_id`, `mapel_id`) VALUES
(8, 'jadwal10', 1, 1, 1, 2, 3),
(14, 'jadwal10', 2, 1, 1, 1, 1),
(15, 'jadwal11', 3, 1, 3, 1, 1),
(16, 'jadwal10', 4, 1, 2, 1, 2),
(17, 'jadwal13', 5, 1, 1, 1, 1),
(18, 'jadwal10', 6, 1, 1, 1, 2),
(20, 'jadwal10', 1, 2, 3, 1, 2),
(23, 'jad1', 1, 3, 1, 1, 2);

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_siswa`
--

CREATE TABLE `penjadwalan_siswa` (
  `id` int(11) NOT NULL,
  `nis` varchar(15) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `nama_blkg` varchar(50) NOT NULL,
  `kelas_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_siswa`
--

INSERT INTO `penjadwalan_siswa` (`id`, `nis`, `nama`, `nama_blkg`, `kelas_id`, `user_id`) VALUES
(1, '1234', 'Ucup', 'Bambank', 1, 4),
(2, '2323', 'selpong', 'wqwq', 2, 6);

-- --------------------------------------------------------

--
-- Table structure for table `penjadwalan_surat_ijin`
--

CREATE TABLE `penjadwalan_surat_ijin` (
  `id` int(11) NOT NULL,
  `judul` varchar(200) NOT NULL,
  `isi` longtext NOT NULL,
  `tgl_post` datetime(6) NOT NULL,
  `pengirim` varchar(200) NOT NULL,
  `dokumen` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `penjadwalan_surat_ijin`
--

INSERT INTO `penjadwalan_surat_ijin` (`id`, `judul`, `isi`, `tgl_post`, `pengirim`, `dokumen`) VALUES
(4, 'Ijin sakit', 'dfghjkmnbv', '2020-01-10 11:32:24.000000', '1', 'static/doc_suratijin/turnitin.PNG'),
(5, 'Pengajian Rutin Ahad Pagi', 'dfgdfz', '2020-01-11 04:24:10.000000', 'dfg', 'pic_folder/None/no-img.jpg'),
(6, 'Baitul Arqom Kepala Sekolah dan Ortom Muhammadiyah', 's', '2020-01-11 05:12:38.000000', 'pengirim', 'pic_folder/None/no-img.jpg');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `penjadwalan_guru`
--
ALTER TABLE `penjadwalan_guru`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nik` (`nik`),
  ADD UNIQUE KEY `kode` (`kode`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `penjadwalan_hari`
--
ALTER TABLE `penjadwalan_hari`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penjadwalan_kelas`
--
ALTER TABLE `penjadwalan_kelas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penjadwalan_mapel`
--
ALTER TABLE `penjadwalan_mapel`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penjadwalan_pengumuman`
--
ALTER TABLE `penjadwalan_pengumuman`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `penjadwalan_penjadwalan`
--
ALTER TABLE `penjadwalan_penjadwalan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `penjadwalan_penjadwalan_guru_id_852883cc_fk_penjadwalan_guru_id` (`guru_id`),
  ADD KEY `penjadwalan_penjadwa_kelas_id_dfcd55e1_fk_penjadwal` (`kelas_id`),
  ADD KEY `penjadwalan_penjadwa_mapel_id_416167be_fk_penjadwal` (`mapel_id`);

--
-- Indexes for table `penjadwalan_siswa`
--
ALTER TABLE `penjadwalan_siswa`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nis` (`nis`),
  ADD UNIQUE KEY `user_id` (`user_id`),
  ADD KEY `penjadwalan_siswa_kelas_id_6f695424_fk_penjadwalan_kelas_id` (`kelas_id`);

--
-- Indexes for table `penjadwalan_surat_ijin`
--
ALTER TABLE `penjadwalan_surat_ijin`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `penjadwalan_guru`
--
ALTER TABLE `penjadwalan_guru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `penjadwalan_hari`
--
ALTER TABLE `penjadwalan_hari`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `penjadwalan_kelas`
--
ALTER TABLE `penjadwalan_kelas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `penjadwalan_mapel`
--
ALTER TABLE `penjadwalan_mapel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `penjadwalan_pengumuman`
--
ALTER TABLE `penjadwalan_pengumuman`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `penjadwalan_penjadwalan`
--
ALTER TABLE `penjadwalan_penjadwalan`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `penjadwalan_siswa`
--
ALTER TABLE `penjadwalan_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `penjadwalan_surat_ijin`
--
ALTER TABLE `penjadwalan_surat_ijin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `penjadwalan_guru`
--
ALTER TABLE `penjadwalan_guru`
  ADD CONSTRAINT `penjadwalan_guru_user_id_787eb899_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `penjadwalan_penjadwalan`
--
ALTER TABLE `penjadwalan_penjadwalan`
  ADD CONSTRAINT `penjadwalan_penjadwa_kelas_id_dfcd55e1_fk_penjadwal` FOREIGN KEY (`kelas_id`) REFERENCES `penjadwalan_kelas` (`id`),
  ADD CONSTRAINT `penjadwalan_penjadwa_mapel_id_416167be_fk_penjadwal` FOREIGN KEY (`mapel_id`) REFERENCES `penjadwalan_mapel` (`id`),
  ADD CONSTRAINT `penjadwalan_penjadwalan_guru_id_852883cc_fk_penjadwalan_guru_id` FOREIGN KEY (`guru_id`) REFERENCES `penjadwalan_guru` (`id`);

--
-- Constraints for table `penjadwalan_siswa`
--
ALTER TABLE `penjadwalan_siswa`
  ADD CONSTRAINT `penjadwalan_siswa_kelas_id_6f695424_fk_penjadwalan_kelas_id` FOREIGN KEY (`kelas_id`) REFERENCES `penjadwalan_kelas` (`id`),
  ADD CONSTRAINT `penjadwalan_siswa_user_id_b6007c1e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
