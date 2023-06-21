/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.7.9 : Database - online_integrated_education
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`online_integrated_education` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `online_integrated_education`;

/*Table structure for table `assignments` */

DROP TABLE IF EXISTS `assignments`;

CREATE TABLE `assignments` (
  `assignment_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `ass_description` varchar(50) DEFAULT NULL,
  `ass_date` date DEFAULT NULL,
  `last_date_sub` date DEFAULT NULL,
  `max_mark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`assignment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `assignments` */

insert  into `assignments`(`assignment_id`,`teacher_id`,`title`,`ass_description`,`ass_date`,`last_date_sub`,`max_mark`) values (2,1,'Database Design ','Design Data','2022-04-30','2022-05-07','100');

/*Table structure for table `attendence` */

DROP TABLE IF EXISTS `attendence`;

CREATE TABLE `attendence` (
  `atten_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`atten_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendence` */

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `college_id` int(11) NOT NULL AUTO_INCREMENT,
  `college_name` varchar(50) DEFAULT NULL,
  `image` varchar(500) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`college_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`college_id`,`college_name`,`image`,`description`,`address`,`email`,`phone`) values (1,'MACFAST','static/uploads/759543e5-5922-4e1d-8f07-a64a2cc4c635Bcube_sea_1920x1200.jpg','Mar Athanasious College for Advanced Studies..','Thiruvalla,Pathanamthitta','macfast.arg@gmail.com','9897899900');

/*Table structure for table `comments` */

DROP TABLE IF EXISTS `comments`;

CREATE TABLE `comments` (
  `comm_id` int(11) NOT NULL AUTO_INCREMENT,
  `submit_id` int(11) DEFAULT NULL,
  `comment_desc` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`comm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `comments` */

/*Table structure for table `courses` */

DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `department_id` int(11) DEFAULT NULL,
  `course_title` varchar(50) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `courses` */

insert  into `courses`(`course_id`,`department_id`,`course_title`,`description`) values (1,1,'BCA','Bachelor of Computer Applications'),(2,1,'BSC','Bachelor of Computer Science');

/*Table structure for table `departments` */

DROP TABLE IF EXISTS `departments`;

CREATE TABLE `departments` (
  `department_id` int(11) NOT NULL AUTO_INCREMENT,
  `college_id` int(11) DEFAULT NULL,
  `dep_name` varchar(50) DEFAULT NULL,
  `dep_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `departments` */

insert  into `departments`(`department_id`,`college_id`,`dep_name`,`dep_description`) values (1,1,'Computer Science','Computer Science');

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exam_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `exam_title` varchar(50) DEFAULT NULL,
  `exam_start_date` date DEFAULT NULL,
  `exam_end_date` date DEFAULT NULL,
  `exam_des` varchar(500) DEFAULT NULL,
  `exam_type` varchar(50) DEFAULT NULL,
  `exam_status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`exam_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exam_id`,`course_id`,`exam_title`,`exam_start_date`,`exam_end_date`,`exam_des`,`exam_type`,`exam_status`) values (1,1,'Semester Exmaination','2022-04-30','2022-05-06','asddd','Semester','pending');

/*Table structure for table `fee` */

DROP TABLE IF EXISTS `fee`;

CREATE TABLE `fee` (
  `fee_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `fee` varchar(50) DEFAULT NULL,
  `duration` varchar(50) DEFAULT NULL,
  `sem` varchar(50) DEFAULT NULL,
  `total_amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `fee` */

insert  into `fee`(`fee_id`,`course_id`,`fee`,`duration`,`sem`,`total_amount`) values (3,1,'36000','3','6','216000');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

insert  into `feedback`(`feedback_id`,`student_id`,`feedback`,`reply`,`date`) values (1,2,'Helooo....','pending','2022-05-02');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `usertype` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values (1,'admin','admin','admin'),(2,'bency','bency','teacher'),(4,'bless','bless','Student'),(5,'libi','libi','teacher');

/*Table structure for table `messages` */

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `message_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  PRIMARY KEY (`message_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `messages` */

insert  into `messages`(`message_id`,`student_id`,`teacher_id`,`message`,`reply`,`date`) values (1,4,1,'assss','pending','2022-05-02 00:00:00');

/*Table structure for table `note` */

DROP TABLE IF EXISTS `note`;

CREATE TABLE `note` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `note_title` varchar(50) DEFAULT NULL,
  `upload_file` varchar(500) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `note` */

insert  into `note`(`note_id`,`teacher_id`,`note_title`,`upload_file`,`date`) values (2,1,'Note1','static/uploads/ad57cf96-3816-48ee-8ae6-50dd7d2491c0Alachamist-Paulo Cohello.pdf','2022-05-02');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `note_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`note_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`note_id`,`notification`,`date`) values (2,'asddddd','2022-04-28');

/*Table structure for table `payment` */

DROP TABLE IF EXISTS `payment`;

CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `fee_id` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `pay_status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `payment` */

/*Table structure for table `stud_submission` */

DROP TABLE IF EXISTS `stud_submission`;

CREATE TABLE `stud_submission` (
  `submit_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  `file_path` varchar(1000) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`submit_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `stud_submission` */

insert  into `stud_submission`(`submit_id`,`student_id`,`type_id`,`file_path`,`status`,`date`,`type`) values (1,2,2,'static/uploads1/248464f7-3bdc-4f9a-85d9-1b035895e22fEnte Kadha-Madavikutty.pdf','Submitted','2022-05-02','Assignment'),(2,2,2,'static/uploads1/c8270133-6d86-4b7c-863e-4d9704e1bd15BalayakalaSakhi-Basheer.pdf','Submitted','2022-05-02','Assignment'),(3,2,2,'static/uploads1/f75b1e5b-b323-49e2-bad9-b7eaceee8790Ente Kadha-Madavikutty.pdf','Submitted','2022-05-02','Assignment'),(4,2,2,'static/uploads1/be4077e0-c434-42ce-b071-3ff3c05ae5d6Ente Kadha-Madavikutty.pdf','Submitted','2022-05-02','Assignment'),(5,2,1,'static/uploads1/7bf6a8f7-ec8b-477b-823b-29dde89bb2bed144658198f4cb5ef4793f056f8d4834.jpg','Submitted','2022-05-02','Task'),(6,2,1,'static/uploads1/0ac86f49-9b36-4f97-9515-537f1c3932b1d144658198f4cb5ef4793f056f8d4834.jpg','Submitted','2022-05-02','Task');

/*Table structure for table `students` */

DROP TABLE IF EXISTS `students`;

CREATE TABLE `students` (
  `student_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `students` */

insert  into `students`(`student_id`,`login_id`,`course_id`,`firstname`,`lastname`,`address`,`dob`,`email`,`phone`) values (2,4,1,'Blesson','Baby','Modiyil','1996-08-20','bless@gmail.com','9897899906');

/*Table structure for table `subjects` */

DROP TABLE IF EXISTS `subjects`;

CREATE TABLE `subjects` (
  `subject_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_id` int(11) DEFAULT NULL,
  `sub_name` varchar(50) DEFAULT NULL,
  `sub_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`subject_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `subjects` */

insert  into `subjects`(`subject_id`,`course_id`,`sub_name`,`sub_description`) values (1,1,'DBMS','aww'),(2,1,'User Interface','abcd..');

/*Table structure for table `task` */

DROP TABLE IF EXISTS `task`;

CREATE TABLE `task` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) DEFAULT NULL,
  `task_title` varchar(50) DEFAULT NULL,
  `task_des` varchar(500) DEFAULT NULL,
  `task_sub_date` date DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `task` */

insert  into `task`(`task_id`,`teacher_id`,`task_title`,`task_des`,`task_sub_date`) values (1,1,'Title1',' asddd','2022-05-02'),(2,1,'Title1','asss','2022-04-30');

/*Table structure for table `teachers` */

DROP TABLE IF EXISTS `teachers`;

CREATE TABLE `teachers` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `subject_id` int(11) DEFAULT NULL,
  `firstname` varchar(50) DEFAULT NULL,
  `lastname` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `teachers` */

insert  into `teachers`(`teacher_id`,`login_id`,`subject_id`,`firstname`,`lastname`,`qualification`,`gender`,`email`,`phone`) values (1,2,1,'Bency','Baby','MCA','female','bency@gmail.com','9897899901'),(2,5,2,'Libin',' Mathew','PHD','male','libi@gmail.com','9196564323');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
