
(cl:in-package :asdf)

(defsystem "markerlocator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "markerpose" :depends-on ("_package_markerpose"))
    (:file "_package_markerpose" :depends-on ("_package"))
  ))