resource "tfe_workspace" "{{ workspace }}" {
    allow_destroy_plan    = {{ workspace.allow_destroy_plan|lower }}
    auto_apply            = {{ workspace.auto_apply|lower }}
    {% if workspace.exection_mode -%}
    execution_mode        = "{{ workspace.execution_mode }}"
    {% endif %}
    file_triggers_enabled = {{ workspace.file_triggers_enabled|lower }}
    name                  = "{{ workspace.name }}"
    organization          = "{{ workspace.organization }}"
    {% if workspace.operations -%}
    operations            = {{ workspace.operations|lower }}
    {% endif %}
    queue_all_runs        = {{ workspace.queue_all_runs|lower }}
    speculative_enabled   = {{ workspace.speculative_enabled|lower }}
    trigger_prefixes      = {{ workspace.trigger_prefixes }}
    terraform_version     = "{{ workspace.terraform_version }}"
    {% if workspace.working_directory -%}
    working_directory     = "{{ workspace.working_directory }}"
    {% endif %}
    {% if has_vcs -%}
    vcs_repo {
        identifier         = "{{ vcs_repo.identifier }}"
        ingress_submodules = {{ vcs_repo.ingress_submodules|lower }}
        oauth_token_id     = "{{ vcs_repo.oauth_token_id }}"
        branch             = "{{ vcs_repo.branch|default("master") }}"
    }
    {% endif %}
}
