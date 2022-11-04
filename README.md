# SECURITY VERIFICATION IN ROS - *svROS*

Verification of security in robotic systems is one of the most difficult tasks from the standpoint of software development, as it might lead to a variety of loose ends. However, it has been shown how security hyperproperties, in particular Observational Determinism, can be verified by resorting to the use of formal methods.

Using formal frameworks for verification, such as Alloy, requires a significant level of expertise, which a common ROS developer does not possess. In addition, no state-of-art tool contemplates techniques to formally verify security in ROS2, which naturally motivates the study considered within the scope of this dissertation.

Therefore, a verification tool was developed, named Security Verification in ROS (svROS), which focuses on abstracting formal verification approaches, to provide a less-formal, easier to use, solution to verify OD in ROS2 system applications. To check the correctness of a ROS application behaviour in respect to OD, it is necessary to specify how the system behaves atomically in each node. For this, the tool incorporates a specification language that is more user-friendly than Alloy and, it enables the specification of intra-node operations, in respect to the publish-subscribe paradigm.

svROS supports the following capabilities:
* Source code fetching from ROS2 application packages.
* Reverse engineering methods to infer an architecture topology from the extracted code.
* Generation of configuration file templates, to allow a ROS developer to easily configure its application network.
* Methods to translate the system configuration into a model in Alloy, to later perform the verification of OD.
* A domain specific language to specify the intra-node behaviour of a ROS application, and methods to translate such specifications into Alloy.

Enjoy! (ง ͡❛ ͜ʖ ͡❛)ง
