from support.utils.file_system import FileSystem


def prepare_directories() -> None:
    """
    Function for create dirs for reports
    :return: None
    """
    FileSystem.delete_dir('reports', 'advisor-smoke-results-android', 'results')
    FileSystem.delete_dir('reports', 'advisor-smoke-results-ios', 'results')
    FileSystem.delete_dir('reports', 'advisor-acceptance-results-android', 'results')
    FileSystem.delete_dir('reports', 'advisor-acceptance-results-ios', 'results')
    FileSystem.delete_dir('reports', 'advisor-regression-results-android', 'results')
    FileSystem.delete_dir('reports', 'advisor-regression-results-ios', 'results')
    FileSystem.make_dir('reports', 'advisor-smoke-results-android', 'results')
    FileSystem.make_dir('reports', 'advisor-smoke-results-ios', 'results')
    FileSystem.make_dir('reports', 'advisor-acceptance-results-android', 'results')
    FileSystem.make_dir('reports', 'advisor-acceptance-results-ios', 'results')
    FileSystem.make_dir('reports', 'advisor-regression-results-android', 'results')
    FileSystem.make_dir('reports', 'advisor-regression-results-ios', 'results')


if __name__ == "__main__":
    prepare_directories()
