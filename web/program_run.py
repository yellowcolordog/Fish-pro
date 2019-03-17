from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3306/Blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True


db = SQLAlchemy(app)

# create table user01(
#     user_id int primary key auto_increment,
#     user_account varchar(16) not null,
#     user_password varchar(16) not null,
#     user_name varchar(32) not null,  -- 加索引
#     user_phone varchar(16) not null,
#     user_email varchar(32),    
#     user_sex int not null,
# );


# 1.1用户基本信息表
class User01(db.Model):
    __tablename__ = 'user01'
    user_id = db.Column(db.Integer,primary_key = True)
    user_phone = db.Column(db.String(32),nullable = False)
    user_password = db.Column(db.String(16),nullable = False)
    user_name = db.Column(db.String(32),nullable = False)
    user_email = db.Column(db.String(16),nullable = True)
    user_sex = db.Column(db.Boolean,nullable = False,default = True)





# 1.2 用户头像表, 存路径
class User_head_path(db.Model):
    __tablename__='user_head_path'
    user_head_path_id = db.Column(db.String(32),primary_key = True)
    user_head_path = db.Column(db.String(300),nullable = True)

# create table note01(
#     note_id int primary key auto_increment,
#     note_create_date datetime default now(), 
#     note_creater_id int not null,
#     note_creater_name varchar(32) not null,
#     note_title varchar(32) not null,
#     note_raise int,  --点赞
#     note_down int  --差评
# )

# 1.3用户/用户关注表
class User_user_attention(db.Model):
    __tablename__ = 'user_attention'
    user_attention_id = db.Column(db.Integer,primary_key = True)
    user_idol_id = db.Column(db.Integer,nullable = False)
    note_idol_name = db.Column(db.String(32),nullable = False)
    user_fans_id = db.Column(db.Integer,nullable = False)
    note_fans_name = db.Column(db.String(32),nullable = False)

# 1.4 用户/帖子关注表
class User_note_attention(db.Model):
    __tablename__ = 'note_attention'
    note_attention_id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,nullable = False)
    note_id = db.Column(db.Integer,nullable = False)


# 2.1帖子基本信息表
class Note01(db.Model):
    __tablename__ = 'Note01'
    note_id = db.Column(db.Integer,primary_key = True)
    note_creater_id = db.Column(db.Integer,nullable = False)
    note_create_date = db.Column(db.DateTime,nullable = False,index = True)
    note_creater_name = db.Column(db.String(32),nullable = False)
    note_title = db.Column(db.String(32),nullable = False)
    note_raise = db.Column(db.Integer,nullable = True)
    note_down = db.Column(db.Integer,nullable = True)


# create table note_content(
#     note_content_id int primary key auto_increment,
#     note_id int not null,
#     note_content_word varchar(600),
#     note_content_file1 
# )


# 2.2帖子内容表
class Note_content(db.Model):
    __tablename__ = 'Note_content'
    note_content_id = db.Column(db.Integer,primary_key = True)
    note_id =  db.Column(db.Integer,nullable = False)
    note_content_word = db.Column(db.String(600),nullable = True)
    note_content_file = db.Column(db.String(300),nullable = True)

# 3.1帖子评论表
class Note_comment(db.Model):
    __tablename__ = 'note_comment'
    comment_id = db.Column(db.Integer,primary_key = True)
    comment_date = db.Column(db.DateTime,nullable = False,index = True)
    comment_user_id = db.Column(db.Integer,nullable = False)
    comment_content = db.Column(db.String(600),nullable = False)
    comment_raise = db.Column(db.Integer,nullable = True)
    comment_down = db.Column(db.Integer,nullable = True)
    commentator_id = db.Column(db.Integer,nullable = True)

# 登录
@app.route('/login',methods=['GET','POST'])
def login_views():
    if request.method =='GET':
        return render_template('login.html')
    else:
        user = User01()
        r = request.form
        user.user_phone = int(r['login_phone'])
        user.user_name = r['login_name']
        user.user_password = r['login_pwd']
        user.user_email = r['login_email']
        
        db.session.add(user)
        return render_template('register_success.html')


@app.route('/login_phone')
def login_phone_views():
    login_phone = request.args['login_phone']
    # 2. 验证数据是否存在
    u = User01.query.filter_by(user_phone=login_phone).first()
    print(login_phone)
    # 3. 根据结果给出返回值
    if u:
        return '1' # 用户名已存在
    else:
        return '0' # 用户名不存在




if __name__ == '__main__':
    app.run(debug=True,port=7777)