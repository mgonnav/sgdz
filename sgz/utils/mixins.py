from rest_framework.response import Response


class PaginatedCustomOrderingMixin:
    """
    Apply this mixin to any view or viewset to get paginated results with
    custom filtering based on a `default_ordering` attribute which should be part of the
    model where the search is being performed.
    """

    def list(self, request, *args, **kwargs):
        ordering = request.query_params.get("ordering", self.lookup_field)
        page = self.paginate_queryset(self.queryset.order_by(ordering))
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(page, many=True)
        return Response(serializer.data)


class PartialRetrieveMixin:
    """
    Apply this mixin to any view or viewset to get partial results when searching
    using the `lookup_field` attribute which should be part of the model where the
    search is being performed.
    """

    def retrieve(self, request, *args, **kwargs):
        keyword = kwargs.get(self.lookup_field, "")
        results = self.queryset.filter(**{f"{self.lookup_field}__icontains": keyword})
        serializer = self.get_serializer(results, many=True)
        return Response(serializer.data[:10])
