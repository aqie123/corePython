public function registerAction(){
 33         // todo 实现用户注册
 34 
 35         $uname = $this->getRequest()->getPost('uname',false);
 36         $pwd = $this->getRequest()->getPost('pwd',false);
 37         if (!$uname || $pwd){
 38             echo json_encode(array('error'=>-1002,'errmsg'=>'用户名与密码必填'));
 39             return false;
 40         }
 41         // 调用user创建登录验证
 42         $model = new UserModel();
 43         if($model->register(trim($uname),trim($pwd))){
 44             echo json_encode(array(
 45                 'errno'=>0,
 46                 'errmsg'=>'',
 47                 'data'=>array('name'=>$uname)
 48             ));
 49         }else{
 50             echo json_encode(array(
 51                 'errno'=>$model->errno;
 52                 'errmsg'=>$model->errmsg;
 53    
 54             ));
 55         }
 56         return true;
 57     }
