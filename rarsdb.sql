
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `rarsdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `account_holder_details`
--

CREATE TABLE IF NOT EXISTS `account_holder_details` (
  `first_name` varchar(10) NOT NULL,
  `last_name` varchar(10) NOT NULL,
  `user_id` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `password` varchar(15) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `address` varchar(50) NOT NULL,
  `city` varchar(20) NOT NULL,
  `state` varchar(20) NOT NULL,
  `pincode` int(10) NOT NULL,
  `phone` varchar(15) NOT NULL,
  PRIMARY KEY (`user_id`),
  UNIQUE KEY `user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `admin_details`
--

CREATE TABLE IF NOT EXISTS `admin_details` (
  `admin_id` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `admin_password` varchar(15) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_details`
--

INSERT INTO `admin_details` (`admin_id`, `admin_password`) VALUES
('Rarsadmin', 'Welcome#2');

-- --------------------------------------------------------

--
-- Table structure for table `license_details`
--

CREATE TABLE IF NOT EXISTS `license_details` (
  `license_no` varchar(30) NOT NULL,
  `user_id` varchar(10) NOT NULL,
  `driver_name` varchar(15) NOT NULL,
  `issue_year` int(4) NOT NULL,
  `expire_year` int(4) NOT NULL,
  `issue_authority` varchar(30) NOT NULL,
  `vehicle_type` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `temp_details`
--

CREATE TABLE IF NOT EXISTS `temp_details` (
  `vname` varchar(20) NOT NULL,
  `user_id` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `vtype` varchar(10) NOT NULL,
  `vmodel` varchar(10) NOT NULL,
  `vprice` varchar(15) NOT NULL,
  `vowner` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `transfer_details`
--

CREATE TABLE IF NOT EXISTS `transfer_details` (
  `user_id` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `vyear` int(4) NOT NULL,
  `vnumber` varchar(15) NOT NULL,
  `vnowner` varchar(20) NOT NULL,
  `vprice` varchar(20) NOT NULL,
  `vpowner` varchar(20) NOT NULL,
  `vtype` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `vehicle_details`
--

CREATE TABLE IF NOT EXISTS `vehicle_details` (
  `user_id` varchar(10) CHARACTER SET latin1 COLLATE latin1_general_cs NOT NULL,
  `vehicle_no` varchar(20) NOT NULL,
  `vehicle_type` varchar(10) NOT NULL,
  `vehicle_name` varchar(10) NOT NULL,
  `vehicle_model` varchar(15) NOT NULL,
  `vehicle_color` varchar(10) NOT NULL,
  `vehicle_owner` varchar(15) NOT NULL,
  `vehicle_year` int(4) NOT NULL,
  `sale_state` varchar(20) NOT NULL,
  `sale_date` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
