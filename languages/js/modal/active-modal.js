$(document).ready(function () {
    {# Opening of modal action #}
    $('#actionsModal').on('show.bs.modal', function (event) {

        let button = $(event.relatedTarget); // Button that triggered the modal
        console.log("button: " + button);
        let recipient = button.data('whatever'); // Extract info from data-* attributes

        let rel = event.relatedTarget.parentNode;
        let rel_obj = {
            node_td: rel,
            node_tr: rel.parentNode,
            node_tbody: rel.parentNode.parentNode,
            node_tbody_cl: rel.parentNode.parentNode.className,
            node_table: rel.parentNode.parentNode.parentNode,
            node_table_cl: rel.parentNode.parentNode.parentNode.className,
        };
        {#console.log(`related_target_parent: ${rel_obj}`);#}
        console.table(rel_obj.node_tr.cells);
        console.log("tkn_branch:"+rel_obj.node_tr.cells['tkn_branch'].textContent);
        console.log("pattern_library:"+rel_obj.node_tr.cells['pattern_library'].textContent);
        console.log("pattern_folder_name:"+rel_obj.node_tr.cells['pattern_folder_name'].textContent);
        console.log("addm_name:"+rel_obj.node_tr.cells['addm_name'].textContent);
        console.log("case_id:"+rel_obj.node_tr.cells['case_id'].textContent);

        {% comment %}let cur = event.currentTarget.parentNode;
        let cur_obj = {
            nodeName: cur.nodeName,
            nodeName_cl: cur.className,
            node_1: rel.parentNode.parentNode.nodeName,
            node_1_cl: rel.parentNode.parentNode.className,
            node_2: rel.parentNode.parentNode.parentNode.nodeName,
            node_2_cl: rel.parentNode.parentNode.parentNode.className,
        };
        console.log(`current_target_parent: ${JSON.stringify(cur_obj)}`);
        {% endcomment %}

        {% comment %}Get needed data from table row where button pressed:{% endcomment %}
        {% comment %}console.log("querySelector: tkn_branch" + document.querySelector("#tkn_branch").value);
        console.log("querySelector: pattern_library" + document.querySelector("#pattern_library").value);
        console.log("querySelector: pattern_folder_name" + document.querySelector("#pattern_folder_name").value);
        console.log("querySelector: addm_name" + document.querySelector("#addm_name").value);{% endcomment %}

        {% comment %}console.log("getElementById: tkn_branch" + document.getElementById("tkn_branch"));
        console.log("getElementById: pattern_library" + document.getElementById("pattern_library"));
        console.log("getElementById: pattern_folder_name" + document.getElementById("pattern_folder_name"));
        console.log("getElementById: addm_name" + document.getElementById("addm_name"));

        console.log("getElementById: tkn_branch" + document.getElementById("tkn_branch"));
        console.log("getElementById: pattern_library" + document.getElementById("pattern_library"));
        console.log("getElementById: pattern_folder_name" + document.getElementById("pattern_folder_name"));
        console.log("getElementById: addm_name" + document.getElementById("addm_name"));{% endcomment %}

        console.log(`recipient: ${recipient}`);

        // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
        // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
        let modal = $(this);

        modal.find('.modal-variables').text('New message to ' + recipient);
        {#modal.find('.modal-variables').val(recipient);#}
    })
});
