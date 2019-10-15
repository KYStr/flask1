function upload(k, w, h, url) {
    $("#upload_" + k).click(function () {
        var img = $("#file_" + k)[0].files[0];
        var csrf_token = $('input[name="csrf_token"]').val();
        console.log(img);
        console.log(csrf_token);
        if (img) {
            var formData = new FormData();
            formData.append("image", img);
            $.ajax({
                url: url,
                type: "POST",
                dataType: "json",
                cache: false,
                contentType: false,
                processData: false,
                headers: {
                    'X-CSRFToken': csrf_token
                },
                data: formData,
                success: function (res) {
                    if (res.code == 1) {
                        var img = res.image;
                        var content = "<img src='/static/uploads/" + img + "' style='width: 200px;height: 200px;'>";
                        $("#image_" + k).empty();
                        $("#image_" + k).append(content);
                        $("#input_" + k).attr('value', img);
                    }
                }
            })
        }
    });
}