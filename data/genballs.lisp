(defpackage foo
  (:use #:cl)
  (:local-nicknames (#:sera #:serapeum)
                    (#:alex #:alexandria)
                    (#:si   #:stateless-iterators))
  (:export #:centers
           #:balls))
(in-package :foo)

(sera:-> list->array (list)
         (values (simple-array single-float (*)) &optional))
(defun list->array (list)
  (make-array (length list)
              :element-type 'single-float
              :initial-contents list))

(sera:-> centers (alex:positive-fixnum alex:positive-fixnum)
         (values list &optional))
(defun centers (n dim)
  (loop repeat n collect
        (list->array
         (loop repeat dim collect (random 1.0)))))

(sera:-> indices-iterator (alex:positive-fixnum alex:positive-fixnum)
         (values si:iterator &optional))
(defun indices-iterator (n dim)
  (si:imap
   #'alex:flatten
   (reduce
    #'si:product
    (loop repeat dim collect (si:range 0 n)))))

(sera:-> distance ((simple-array single-float (*))
                   (simple-array single-float (*)))
         (values single-float &optional))
(defun distance (p1 p2)
  (declare (optimize (speed 3)))
  (sqrt
   (loop for x1 across p1
         for x2 across p2
         for diff = (abs (- x1 x2))
         sum (expt (min diff (- 1 diff)) 2)
         single-float)))

(sera:-> balls (list alex:positive-fixnum
                     alex:positive-fixnum
                     single-float)
         (values (simple-array bit) &optional))
(defun balls (centers n dim radius)
  (let ((result (make-array (loop repeat dim collect n)
                            :element-type 'bit))
        (tree (vp-trees:make-vp-tree centers #'distance))
        (iter (indices-iterator n dim)))
    (si:do-iterator (index iter)
      (setf (apply #'aref result index)
            (if (vp-trees:items-in-ball
                 tree
                 (list->array
                  (mapcar
                   (lambda (i) (float (/ i n)))
                   index))
                 radius
                 #'distance)
                1 0)))
    result))
