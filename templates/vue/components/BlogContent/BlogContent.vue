<template>
    <div id="blogs" :data="bloglist">
        <div id="blog-content" class="box mb-3 shadow-sm border rounded bg-white osahan-post can-drag">
        <div class="p-3 d-flex align-items-center border-bottom osahan-post-header">
            <div class="dropdown-list-image mr-3">
                <img class="rounded-circle" slot-scope="scope" src={{scope.row.fields.image}} alt="">
                <div class="status-indicator bg-success"></div>
            </div>
            <div class="font-weight-bold">
                <div class="text-truncate" slot-scope="scope">{{scope.row.fk}}</div>
                <div class="small text-gray-500">Web Developer @Google</div>
            </div>
            <span class="ml-auto small">3 hours</span>
        </div>
        <div class="p-3 border-bottom osahan-post-body">
            <p slot-scope="scope">{{scope.row.fields.content}}</p>
            <img  class="img-fluid" alt="Responsive image" src='../../../../static/img/p1.png'>
        </div>
        <div class="p-3 border-bottom osahan-post-footer">
            <a href="#" class="mr-3 text-secondary" slot-scope="scope"><i class="feather-heart text-danger"></i> {{scope.row.fields.liked_num}}</a>
            <a href="#" class="mr-3 text-secondary"><i class="feather-message-square"></i> 8</a>
            <a href="#" class="mr-3 text-secondary"><i class="feather-share-2"></i> 2</a>
        </div>
        <!--
              评论区//TODO
        -->
        <div class="p-3 d-flex align-items-top border-bottom osahan-post-comment">
            <div class="dropdown-list-image mr-3">
                <img class="rounded-circle" alt="" src='../../../../static/img/p1.png' >
                <div class="status-indicator bg-success"></div>
            </div>
            <div class="font-weight-bold">
                <div class="text-truncate"> James Spiegel <span class="float-right small">2 min</span></div>
                <div class="small text-gray-500">Ratione voluptatem sequi en lod nesciunt. Neque porro quisquam est,
                    quinder dolorem ipsum quia dolor sit amet, consectetur
                </div>
            </div>
        </div>


        <div class="p-3">
            <label>
                <textarea placeholder="Add Comment..." class="form-control border-0 p-0 shadow-none" rows="1"></textarea>
            </label>
        </div>
    </div>
    </div>
</template>
<script>
    export default{
        name:'blog_content',
        data(){
            return{
                bloglist:[],
                commentslist:[],
                isCommentOpening: false,
                message:'',
            }
        },
        mounted(){
            this.showBlog()
        },
        methods:{
            showBlog(){
                this.axios.get('/article/show').then((response)=>{
                    let res = JSON.parse(response.bodyText);
                    if(res.error_num ===0) this.bloglist = res['list'];
                    else {
                        this.$message.error("加载博客失败");
                        this.message = res['msg']
                    }
                })
            },

            addComment(){

            }

        }
    }
</script>
<style>

</style>