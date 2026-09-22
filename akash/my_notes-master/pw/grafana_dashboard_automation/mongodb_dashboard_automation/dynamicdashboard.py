from jinja2 import Template

def render_template(template_file, dashboard_name, service_name, output_file):
    with open(template_file, 'r') as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_content = template.render(dashboard_name=dashboard_name, service_name=service_name,redis_shards_endpoint=redis_shards_endpoint,mongodb_endpoint=mongodb_endpoint)

    with open(output_file, 'w') as file:
        file.write(rendered_content)

# Example usage
template_file = 'jinja.json'
dashboard_name =  'Form Service Dashboard'
service_name = 'form-service'
output_file = 'form-service.json' 
redis_shards_endpoint = ["prod-form-redis-cluster-0001-001","prod-form-redis-cluster-0001-002"]
# mongodb_endpoint = ["penpencil-doubt-comment-shard-00-00.qeaxj.mongodb.net","penpencil-doubt-comment-shard-00-01.qeaxj.mongodb.net","penpencil-doubt-comment-shard-00-02.qeaxj.mongodb.net","penpencil-production-se-shard-00-00.qeaxj.mongodb.net","penpencil-production-se-shard-00-01.qeaxj.mongodb.net","penpencil-production-se-shard-00-02.qeaxj.mongodb.net","penpencil-data-logging-shard-00-00.qeaxj.mongodb.net","penpencil-data-logging-shard-00-01.qeaxj.mongodb.net","penpencil-data-logging-shard-00-02.qeaxj.mongodb.net"]
mongodb_endpoint = ["penpencil-saarthi-servi-shard-00-02.qeaxj.mongodb.net","penpencil-saarthi-servi-shard-00-01.qeaxj.mongodb.net","penpencil-saarthi-servi-shard-00-00.qeaxj.mongodb.net"]
render_template(template_file, dashboard_name, service_name, output_file)
print("Rendered template saved to", output_file)